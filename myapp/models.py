from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField(auto_now=True)
    commentaries = models.CharField(max_length=1000)
