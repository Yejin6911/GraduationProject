from django.contrib import admin

# Register your models here.
from alarm.models import Alarm

admin.site.register(Alarm)