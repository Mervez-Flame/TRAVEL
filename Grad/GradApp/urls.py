from django.test import TestCase
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signUpPage', views.signUpPage, name='signUpPage'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('kings/', views.Bookings, name='kings'),
    path('register/', views.register, name='register'),
    # path('about/', views.about, name='about'),
    # path('offers/', views.offers, name='offers'),
    # path('destinations/', views.destinations, name='destinations'),
    path('logout', views.logout,  name='logout')
]
