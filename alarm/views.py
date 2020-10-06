from django.views.generic import TemplateView
from . import models
import json
from django.shortcuts import HttpResponse
from playsound import playsound

from .models import Alarm
from map.models import Location

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


def siren(request):
    playsound("/Users/yejin/dev/GraduationProject/alarm/siren.mp3")
    return HttpResponse('')