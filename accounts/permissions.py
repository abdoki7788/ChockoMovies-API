from rest_framework.permissions import BasePermission

class IsCurrentUserOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser