#### imports
from djoser.serializers import UserSerializer
from djoser.conf import settings

from .models import User
####

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