#### imports
from djoser.serializers import UserSerializer
from djoser.conf import settings

from rest_framework import serializers

from .models import User
from chocko.models import Comment
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

class DashBoardCommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='get_likes_count', read_only=True)
    author = CurrentUserSerializer()
    class Meta:
        model = Comment
        fields = ['id','author', 'target', 'content', 'send_date', 'likes_count']
        extra_kwargs = {'author': {'read_only': True}, 'target': {'required': False}}


class DashBoardSerializer(serializers.Serializer):
    comments_count = serializers.IntegerField()
    requested_movies = serializers.IntegerField()
    saves_count = serializers.IntegerField()
    ip = serializers.IPAddressField()
    registered_date = serializers.DateTimeField()
    last_login_date = serializers.DateTimeField()
    last_comment = serializers.DictField(required=False, default=None)