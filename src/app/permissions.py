from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)


class IsCallCenter(permissions.BasePermission):
    def has_permission(self, request, view):
        user_group = request.user.groups
        if user_group.filter(name='call_center').exists():
            return True
        else:
            logger.warning(f"User {request.user.username} does not have call center permissions")
            return False
