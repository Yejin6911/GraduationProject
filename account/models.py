from django.db import models
from django.contrib.auth.models import AbstractUser

class Station(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return str(self.pk)+'.'+self.name

class CustomUser(AbstractUser):

    station = models.ForeignKey('account.Station', on_delete=models.CASCADE, null=True)

class Guard(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    station = models.ForeignKey('account.Station', on_delete=models.CASCADE)
    state = models.BooleanField(default=False)