from django.contrib import admin
from django.urls import path, include
from alarm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
    path('account/', include('account.urls')),
    path('Alert/', views.Alert.as_view()),
]
