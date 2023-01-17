from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import User
from djoser.conf import settings

class CurrentUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
            'date_joined',
            'profile',
            'about'
        )
        read_only_fields = (settings.LOGIN_FIELD,)