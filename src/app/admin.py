from django.contrib import admin

from .models import Appeal


class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_name', 'phone_number', 'app_datetime', 'created_at')
    search_fields = ('name', 'app_name', 'phone_number')
    list_per_page = 25


admin.site.register(Appeal, AppealAdmin)
