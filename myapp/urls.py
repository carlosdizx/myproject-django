from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('home', views.bookings,)
]
