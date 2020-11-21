from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Station(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return str(self.pk)+'.'+self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    station = models.ForeignKey('account.Station', on_delete=models.CASCADE, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Guard(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    station = models.ForeignKey('account.Station', on_delete=models.CASCADE)
    state = models.BooleanField(default=False)