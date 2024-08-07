from django.contrib import admin

from .models import Appeal, FAQ, Answers, Status


class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_name', 'phone_number', 'app_datetime', 'created_at')
    search_fields = ('name', 'app_name', 'phone_number')
    list_per_page = 25


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'created_at')
    search_fields = ('title', 'question')
    list_per_page = 25


class ShAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'created_at')
    search_fields = ('title',)
    list_per_page = 25


admin.site.register(Appeal, AppealAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Answers, FAQAdmin)
admin.site.register(Status, ShAdmin)
