from django.contrib import admin

from account.models import CustomUser, Station
from import_export.admin import ImportExportMixin

admin.site.register(CustomUser)

class StationAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Station, StationAdmin)