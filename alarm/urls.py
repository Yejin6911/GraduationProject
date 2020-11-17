# alarms/urls.py
from django.urls import path
from . import views

app_name = 'alarm'

urlpatterns = [
    path('', views.Alert.as_view()),
    path('siren/<int:location_pk>', views.siren, name='siren'),
]