from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import os

from django.urls import reverse

from account.models import CustomUser
from map.models import Location
from alarm.models import Alarm

# path = str(os.getcwd()) + "/map/static/data/"
# file_list = os.listdir(path)
# file_list_csv = [file for file in file_list if file.endswith(".csv")]
#
# data = []
# for file in file_list_csv:
#     full_path = path + str(file)
#     f = open(full_path, "r", encoding='cp949')
#     lines = f.readlines()
#     l = []
#     for line in lines:
#         l.append(line.split(','))
#     f.close()
#     data += l[1:]

def main(request):
    if not request.user.is_authenticated:
        return redirect(reverse("account:login"))
    else:
        current_user = CustomUser.objects.get(username=request.user.username)
        # data = Location.objects.filter(station=current_user.location)
        alarms = Alarm.objects.filter(checked=False).filter(station=current_user.location)
        return render(request, "map/main.html", {'alarms':alarms})


def cctv(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    return render(request, "map/cctv.html", {'location': location})


