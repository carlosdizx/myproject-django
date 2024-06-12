from django.contrib import admin
from .models import DrinkCategory, Drink

# Register your models here.
admin.site.register(DrinkCategory)
admin.site.register(Drink)
