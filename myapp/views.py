from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def drinks(request, drink_name):
    drinks = {
        'moca': 'tipo de café',
        'te': 'tipo de bebida',
        'limonada': 'tipo de refresco',
        'lulada': 'tipo de refresco'
    }
    return HttpResponse(f"<h1>{drink_name}: {drinks[drink_name]}</h1>")
