from django.contrib import admin
from django.urls import path, include
from alarm import views

from django_otp.admin import OTPAdminSite
class OTPAdmin(OTPAdminSite):
    pass

from django.contrib.auth.models import User
from account.models import CustomUser
from django_otp.plugins.otp_totp.models import TOTPDevice

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)


urlpatterns = [
    path('admin/', admin_site.urls),
    path('dadmin/', admin.site.urls),
    path('', include('map.urls')),
    path('account/', include('account.urls')),
    path('Alert/', include('alarm.urls')),

]
