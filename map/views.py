import json
from sqlite3.dbapi2 import Timestamp

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

class SmsSendView(TemplateView):
    # 실제 문자를 보내주는 메서드

    def send_sms(self, phone_number):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'x-ncp-apigw-timestamp': f'{Timestamp}',
            'x-ncp-iam-access-key': f'ncp:sms:kr:260601292957:graduation_project',
            'x-ncp-apigw-signature-v2': f'79a5bec369f24ec699df4607e28be6e6',
        }

        data = {
            'type': 'SMS',
            'contentType': 'COMM',
            'countryCode': '82',
            'from': f'01062169443',
            'to': [
                f'{phone_number}',
            ],
            'content': f'서대문구 이화여대길 순찰 바람'
        }
        print(data)

        requests.post('https://sens.apigw.ntruss.com/sms/v2', headers=headers, json=data)

    def post(self, request):
        try:
            # input_data = json.loads(request.body)
            # input_phone_number = input_data['phone_number']
            input_phone_number = '01048046921'
            exist_phone_number = SendSms.objects.get(phone_number=input_phone_number).phone_number
            # exist_phone_number.save()

            self.send_sms(phone_number=exist_phone_number)
            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except SendSms.DoesNotExist:
            SendSms.objects.create(
                phone_number=input_phone_number,
            ).save()

            self.send_sms(phone_number=input_phone_number)
            return JsonResponse({'message': 'SUCCESS'}, status=200)
