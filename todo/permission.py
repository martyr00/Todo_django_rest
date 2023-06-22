from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """checking user if he is owner todo_card, or he is superuser"""
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

        return bool(request.user and request.user.is_staff)


