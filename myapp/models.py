from django.db import models


class Bebidas(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
