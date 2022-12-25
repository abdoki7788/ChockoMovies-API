from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.contrib.auth.models import User

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True
        return False