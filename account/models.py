from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ Custom User Model"""

    LOCATION_KDG = "강동구"
    LOCATION_KJG = "광진구"
    LOCATION_SDMG = "서대문구"
    LOCATION_JG = "중구"

    LOCATION_CHOICES = (
        (LOCATION_KDG, "강동구"),
        (LOCATION_KJG, "광진구"),
        (LOCATION_SDMG, "서대문구"),
        (LOCATION_JG, "중구")
    )

    location = models.CharField(choices=LOCATION_CHOICES, max_length=50)


