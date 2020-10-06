from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin, ImportExportActionModelAdmin, \
    ImportExportModelAdmin
from import_export.forms import ImportForm, ConfirmImportForm

from .models import Location, SendSms
from account.models import Station
from django import forms


class LocationResource(resources.ModelResource):
    # station = fields.Field(widget=widgets.ForeignKeyWidget(Station, field='name'))
    station = fields.Field(
        column_name='station',
        attribute='station',
        widget=widgets.ForeignKeyWidget(Station, 'name'))

    class Meta:
        fields = ('station',)


class LocationAdmin(ImportExportMixin, admin.ModelAdmin):
    resources_class = LocationResource

admin.site.register(Location, LocationAdmin)
admin.site.register(SendSms)