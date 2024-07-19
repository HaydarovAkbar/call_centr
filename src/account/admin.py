from django.contrib import admin
from django.contrib.auth.models import User, Permission, Group


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(Group)