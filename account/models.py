from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ Custom User Model"""

    STATION_1 = "서울중부경찰서"
    STATION_2 = "서울종로경찰서"
    STATION_3 = "서울남대문경찰서"
    STATION_4 = "서울서대문경찰서"
    STATION_5 = "서울혜화경찰서"
    STATION_6 = "서울용산경찰서"
    STATION_7 = "서울성북경찰서"
    STATION_8 = "서울동대문경찰서"
    STATION_9 = "서울마포경찰서"
    STATION_10 = "서울영등포경찰서"
    STATION_11 = "서울성동경찰서"
    STATION_12 = "서울동작경찰서"
    STATION_13 = "서울광진경찰서"
    STATION_14 = "서울서부경찰서"
    STATION_15 = "서울강북경찰서"
    STATION_16 = "서울금천경찰서"
    STATION_17 = "서울중랑경찰서"
    STATION_18 = "서울강남경찰서"
    STATION_19 = "서울관악경찰서"
    STATION_20 = "서울강서경찰서"
    STATION_21 = "서울강동경찰서"
    STATION_22 = "서울종암경찰서"
    STATION_23 = "서울구로경찰서"
    STATION_24 = "서울서초경찰서"
    STATION_25 = "서울양천경찰서"
    STATION_26 = "서울송파경찰서"
    STATION_27 = "서울노원경찰서"
    STATION_28 = "서울방배경찰서"
    STATION_29 = "서울은평경찰서"
    STATION_30 = "서울도봉경찰서"
    STATION_31 = "서울수서경찰서"

    LOCATION_CHOICES = (
        (STATION_1 , "서울중부경찰서"),
        (STATION_2 , "서울종로경찰서"),
        (STATION_3 , "서울남대문경찰서"),
        (STATION_4 , "서울서대문경찰서"),
        (STATION_5 , "서울혜화경찰서"),
        (STATION_6 , "서울용산경찰서"),
        (STATION_7 , "서울성북경찰서"),
        (STATION_8 , "서울동대문경찰서"),
        (STATION_9 , "서울마포경찰서"),
        (STATION_10, "서울영등포경찰서"),
        (STATION_11, "서울성동경찰서"),
        (STATION_12, "서울동작경찰서"),
        (STATION_13, "서울광진경찰서"),
        (STATION_14, "서울서부경찰서"),
        (STATION_15, "서울강북경찰서"),
        (STATION_16, "서울금천경찰서"),
        (STATION_17, "서울중랑경찰서"),
        (STATION_18, "서울강남경찰서"),
        (STATION_19, "서울관악경찰서"),
        (STATION_20, "서울강서경찰서"),
        (STATION_21, "서울강동경찰서"),
        (STATION_22, "서울종암경찰서"),
        (STATION_23, "서울구로경찰서"),
        (STATION_24, "서울서초경찰서"),
        (STATION_25, "서울양천경찰서"),
        (STATION_26, "서울송파경찰서"),
        (STATION_27, "서울노원경찰서"),
        (STATION_28, "서울방배경찰서"),
        (STATION_29, "서울은평경찰서"),
        (STATION_30, "서울도봉경찰서"),
        (STATION_31, "서울수서경찰서"),
    )

    location = models.CharField(choices=LOCATION_CHOICES, max_length=50)


