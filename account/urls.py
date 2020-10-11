from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
