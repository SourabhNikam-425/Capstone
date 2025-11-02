import os, requests, json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

# Express-Mongo backend base URL (adjust if deployed)
EXPRESS_BASE = os.getenv('EXPRESS_BASE','http://localhost:3001')

def home(request):
    # show all dealers via express endpoint
    resp = requests.get(f"{EXPRESS_BASE}/dealers")
    dealers = resp.json() if resp.status_code == 200 else []
    return render(request, 'home.html', {'dealers': dealers})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Message sent (demo).')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username'); password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have logged out.')
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def dealers_list(request):
    resp = requests.get(f"{EXPRESS_BASE}/dealers")
    dealers = resp.json() if resp.status_code == 200 else []
    return render(request, 'home.html', {'dealers': dealers})

def dealers_by_state(request, state):
    resp = requests.get(f"{EXPRESS_BASE}/dealers/state/{state.upper()}")
    dealers = resp.json() if resp.status_code == 200 else []
    return render(request, 'home.html', {'dealers': dealers, 'filter_state': state.upper()})

def dealer_detail(request, dealer_id):
    resp = requests.get(f"{EXPRESS_BASE}/dealer/{dealer_id}")
    dealer = resp.json() if resp.status_code == 200 else None
    return render(request, 'dealer_detail.html', {'dealer': dealer})

def add_review(request, dealer_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in to add review.')
        return redirect('login')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # in a real app we'd POST to express endpoint to store the review
            review_data = form.cleaned_data
            review_data['name'] = request.user.username
            # sentiment: call local sentiment endpoint
            sentiment_resp = requests.post(request.build_absolute_uri('/sentiment/'), json={'text': review_data['review']})
            sentiment = sentiment_resp.json().get('label') if sentiment_resp.ok else 'neutral'
            review_data['sentiment'] = sentiment
            # Post to express (demo: we will POST to /add-review not implemented on server -> instead print)
            # For this project, we will simulate by calling /dealer/:id endpoint, but real insertion requires update route.
            # Instead — show success and redirect to dealer detail page. (Student may extend by adding POST endpoint.)
            messages.success(request, 'Review prepared (demo). It would be stored to backend in a full implementation.')
            return redirect('dealer_detail', dealer_id=dealer_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'dealer_id': dealer_id})

# Sentiment analyzer view - uses NLTK VADER
@csrf_exempt
def sentiment_view(request):
    import nltk
    try:
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
    except Exception:
        nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        try:
            payload = json.loads(data)
            text = payload.get('text', '')
        except Exception:
            text = request.POST.get('text','')
        sia = SentimentIntensityAnalyzer()
        score = sia.polarity_scores(text)['compound']
        if score >= 0.05: label = 'positive'
        elif score <= -0.05: label = 'negative'
        else: label = 'neutral'
        return JsonResponse({'label': label, 'score': score})
    else:
        from django.http import JsonResponse
        return JsonResponse({'message': 'send POST with JSON {"text": "your text"}'})
