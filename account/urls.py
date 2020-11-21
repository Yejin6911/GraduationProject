from django.urls import path
from django.contrib.auth.views import LoginView
from django_otp.forms import OTPAuthenticationForm

from . import views

app_name = 'account'

urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(authentication_form=OTPAuthenticationForm), name='login'),
    path('logout/', views.logout, name='logout'),
]


