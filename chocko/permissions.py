from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user.is_authenticated and request.user.is_superuser):
            return True
        return False

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_authenticated:
            return True
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or (request.user.is_authenticated and obj.author == request.user):
            return True
        else:
            return False

class IsAdminOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (request.method == 'post' or request.user.is_superuser):
            return True
        return False

class IsAdminOrAuthenticatedCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (request.method not in SAFE_METHODS or request.user.is_superuser):
            return True
        return False