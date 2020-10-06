import json
from sqlite3.dbapi2 import Timestamp

import base64
import hashlib
import hmac
import time
import requests
import json
import keys
from filters import *

import requests.api
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import os

from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from account.models import CustomUser
from map.models import Location, SendSms
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
    # location = Location.objects.get(pk=location_pk)
    alarm = Alarm.objects.filter(location_pk=location_pk).get(checked=False)
    return render(request, "map/cctv.html", {'alarm': alarm})


def check(request, pk):
    alarm = Alarm.objects.get(pk=pk)
    print(alarm)
    alarm.checked = True
    alarm.save()
    return redirect("map:main")

def check(request, location_pk):
    alarm = Alarm.objects.get(location_pk=location_pk)
    print(alarm)
    alarm.checked = True
    alarm.save()
    return redirect("map:main")

def record(request):
    alarms = Alarm.objects.all()
    return render(request, "map/record.html", {'alarms':alarms})

def make_signature(string):
    secret_key = bytes("DHK4IChkpNFoY2YNllWdPg2LQzBnHDLn4ts9USZu", 'UTF-8')
    string = bytes(string, 'UTF-8')
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
    return string_base64


def send(request, alarm_pk):
    url = "https://sens.apigw.ntruss.com"
    uri = "/sms/v2/services/" + "ncp:sms:kr:260601292957:graduation_project" + "/messages"
    api_url = url + uri
    timestamp = str(int(time.time() * 1000))
    access_key = "fnKXlNi1N4YGosnv7usX"
    string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + access_key
    signature = make_signature(string_to_sign)

    alarm = Alarm.objects.get(pk=alarm_pk)
    # 해당 위치의 station을 불러와서, 그 관할서의 guard들을 불러옴.
    address = alarm.address
    station = alarm.station
    guards = guard.objects.filter(station=station)

    message = "{} 관할 구역에서 위급 상황이 발생했습니다. {} 근처에 계신 분들은 신속히 대응해주시기 바랍니다.".format(station, address)

    headers = {
        'Content-Type': "application/json; charset=UTF-8",
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': access_key,
        'x-ncp-apigw-signature-v2': signature
    }


    for guard in guards:
        phone = guard['phone']
        body = {
            "type": "SMS",
            "contentType": "COMM",
            "from": "01048046921",
            "content": message,
            "messages": [{"to": phone}]
        }

        response = requests.post(api_url, headers=headers, data=body)
        response.raise_for_status()

def make_signature(string):
    secret_key = bytes(keys.secret_key, 'UTF-8')
    string = bytes(string, 'UTF-8')
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
    return string_base64