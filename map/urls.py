from django.urls import path, include

from . import views

app_name = 'map'

urlpatterns = [
    path('', views.main, name='main'),
]
