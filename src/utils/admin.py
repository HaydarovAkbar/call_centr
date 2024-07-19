from django.contrib import admin

from .models import Region, District
from django.contrib.admin.models import LogEntry


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['title', 'region']
    list_filter = ['region']
    search_fields = ['title']


admin.site.register(Region)
admin.site.register(District, DistrictAdmin)
admin.site.register(LogEntry, name='Loglar')
