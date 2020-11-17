import socket

from django.views.generic import TemplateView
from . import models
import json
from django.shortcuts import HttpResponse, render
from playsound import playsound
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Alarm
from map.models import Location

@method_decorator(csrf_exempt, name='dispatch')
class Alert(TemplateView):
    template_name = "alarms/alert.html"

    def get_context_data(self, **kwargs):
        context=super(TemplateView, self).get_context_data()
        context['username']=self.request.user.username

        return context

    def post(self, request, **kwargs):
        ins=models.Alarm()
        data_unicode=request.body.decode('utf-8')
        data=json.loads(data_unicode)
        alarms = Alarm.objects.filter(longitude=data['longitude'],latitude=data['latitude']).filter(checked=False)
        if not alarms:
            location = Location.objects.get(longitude=data['longitude'], latitude=data['latitude'])
            if location.S_address != '' or location.S_address!=None:
                ins.address = location.S_address
            else:
                ins.address=location.L_address
            ins.longitude=data['longitude']
            ins.latitude=data['latitude']
            ins.location_pk=location.pk
            ins.station=location.station.name
            ins.save()
        return HttpResponse('')


def siren(request, location_pk):
    try:
        # 서버의 주소입니다. hostname 또는 ip address를 사용할 수 있습니다.
        HOST = '192.168.137.90'
        # 서버에서 지정해 놓은 포트 번호입니다.
        PORT = 9999

        # 소켓 객체를 생성합니다.
        # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
        client_socket.connect((HOST, PORT))

        # 메시지를 전송합니다.
        client_socket.sendall('1'.encode())

        # 메시지를 수신합니다.
        data = client_socket.recv(1024)
        print('Received', repr(data.decode()))

        # 소켓을 닫습니다.
        client_socket.close()
    except ConnectionResetError:
        alarm = Alarm.objects.filter(location_pk=location_pk).get(checked=False)
        return render(request, "map/cctv.html", {'alarm': alarm, 'locatin_pk': location_pk})
    return HttpResponse('')

