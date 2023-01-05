from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomUserViewSet

router = DefaultRouter()
router.register("users", CustomUserViewSet)

urlpatterns = [
    path('', include('djoser.urls.jwt')),
]

urlpatterns += router.urls