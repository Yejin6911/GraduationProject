from django.contrib import admin

from account.models import Profile, Station, Guard
from import_export.admin import ImportExportMixin

admin.site.register(Profile)

class StationAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Station, StationAdmin)

class GuardAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Guard, GuardAdmin)