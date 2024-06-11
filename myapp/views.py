from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def menu_items(request, dish):
    items = {
        'pasta': 'Pasta and cheese',
        'bbq': 'Beef BBQ',
        'fruits': 'Tropical fruits'
    }

    description = items[dish]

    return HttpResponse(f"<h1>{dish}: {description}</h1>")
