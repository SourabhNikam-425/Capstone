from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dealers/', views.dealers_list, name='dealers_list'),
    path('dealers/state/<str:state>/', views.dealers_by_state, name='dealers_by_state'),
    path('dealer/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),
]
