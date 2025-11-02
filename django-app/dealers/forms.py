from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=80)
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1, max_value=5)
    purchase_date = forms.DateField(required=False)
    car_make = forms.CharField(required=False)
    car_model = forms.CharField(required=False)
