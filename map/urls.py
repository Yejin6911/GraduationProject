from django.urls import path, include

from map import views

app_name = 'map'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
]
