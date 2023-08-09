from django.test import TestCase
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signUpPage', views.signUpPage, name='signUpPage'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('Bookings/', views.Bookings, name='Bookings'),
    # path('about/', views.about, name='about'),
    # path('offers/', views.offers, name='offers'),
    # path('destinations/', views.destinations, name='destinations'),
    path('logout', views.logout,  name='logout')
]
