import json
from sqlite3.dbapi2 import Timestamp

import base64
import hashlib
import hmac
import time
import requests
import json
from . import keys

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import os

from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from account.models import CustomUser, Guard, Station
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
from .models import Location


def main(request):
    if not request.user.is_authenticated:
        return redirect(reverse("account:login"))
    else:
        current_user = CustomUser.objects.get(username=request.user.username)
        # data = Location.objects.filter(station=current_user.location)
        alarms = Alarm.objects.filter(checked=False).filter(station=current_user.station.name)
        return render(request, "map/main.html", {'alarms':alarms})

def cctv(request, location_pk):
    # location = Location.objects.get(pk=location_pk)
    alarm = Alarm.objects.filter(location_pk=location_pk).get(checked=False)
    return render(request, "map/cctv.html", {'alarm': alarm, 'location_pk': location_pk})


def check(request, pk):
    alarm = Alarm.objects.get(pk=pk)
    alarm.checked = True
    alarm.save()
    return redirect("map:main")


def record(request):
    current_user = CustomUser.objects.get(username=request.user.username)
    alarms = Alarm.objects.filter(station=current_user.station.name)
    return render(request, "map/record.html", {'alarms':alarms, 'station': current_user.station.name})

def police_list(request):
    current_user = CustomUser.objects.get(username=request.user.username)
    polices = CustomUser.objects.filter(station=current_user.station)
    return render(request, "map/police_list.html", {'polices':polices,'station':current_user.station.name})

def guard_list(request):
    current_user = CustomUser.objects.get(username=request.user.username)
    guards = Guard.objects.filter(station=current_user.station)
    return render(request, "map/guard_list.html", {'guards':guards, 'station':current_user.station.name})

def make_signature(string):
    secret_key = bytes("DHK4IChkpNFoY2YNllWdPg2LQzBnHDLn4ts9USZu", 'UTF-8')
    string = bytes(string, 'UTF-8')
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
    return string_base64

def send(request, alarm_pk):
    url = "https://sens.apigw.ntruss.com"
    uri = "/sms/v2/services/" + keys.service_id + "/messages"
    api_url = url + uri
    timestamp = str(int(time.time() * 1000))
    access_key = keys.access_key
    string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + access_key
    signature = make_signature(string_to_sign)

    alarm = Alarm.objects.get(pk=alarm_pk)
    location = Location.objects.get(pk=alarm.location_pk)
    # 해당 위치의 station을 불러와서, 그 관할서의 guard들을 불러옴.
    address = alarm.address
    station = Station.objects.get(name=alarm.station)
    guards = Guard.objects.filter(station=station.pk)

    message = "{} 확인요망".format(address)

    headers = {
        'Content-Type': "application/json; charset=UTF-8",
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': access_key,
        'x-ncp-apigw-signature-v2': signature
    }


    for guard in guards:
        phone = guard.phone
        body = {
            "type": "SMS",
            "contentType": "COMM",
            "from": "01048046921",
            "content": message,
            "messages": [{"to": phone}]
        }
        body2 = json.dumps(body)
        response = requests.post(api_url, headers=headers, data=body2)
        response.raise_for_status()
    return redirect("map:cctv", location.pk)

def make_signature(string):
    secret_key = bytes(keys.secret_key, 'UTF-8')
    string = bytes(string, 'UTF-8')
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac)
    return string_base64