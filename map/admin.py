from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Location, SendSms


class LocationAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(SendSms)