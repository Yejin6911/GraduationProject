from django.urls import path, include

from . import views

app_name = 'map'

urlpatterns = [
    path('', views.main, name='main'),
    path('cctv/<int:location_pk>', views.cctv, name='cctv'),
    path('cctv/check/<int:pk>', views.check, name='check'),
    path('record/',views.record, name='record'),
]
