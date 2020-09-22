from django.db import models
from map.models import Location

class Alarm(models.Model):
    latitude = models.TextField(null=True)
    longitude = models.TextField(null=True)
    location_pk = models.IntegerField(null=True)
    address = models.TextField(null=True)
    station = models.CharField(max_length=30)
    checked = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)