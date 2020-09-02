from django.db import models

from config import settings


class Location(models.Model):
    management = models.CharField(max_length=30)
    S_address = models.TextField(null=True)
    L_address = models.TextField(null=True)
    purpose = models.TextField(null=True)
    camera_num = models.IntegerField(null=True)
    camera_pixel = models.IntegerField(null=True)
    shoot_info= models.TextField(null=True)
    storage_days = models.IntegerField(null=True)
    installed_date = models.TextField(null=True)
    phone = models.TextField(null=True)
    latitude= models.TextField(null=True)
    longitude = models.TextField(null=True)
    data_date=  models.DateField(null=True)
    alarm = models.BooleanField(default=False)
    station = models.CharField(max_length=30)

    def __str__(self):
        return str(self.pk)+"."+self.station
