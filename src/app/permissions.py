from rest_framework import permissions


class IsCallCenter(permissions.BasePermission):
    def has_permission(self, request, view):
        if 'call_center' in request.user.groups.first().name:
            return True
        elif 'call_center' in request.user.groups.last():
            return True
        else:
            return False
