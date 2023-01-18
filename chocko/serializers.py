from rest_framework import serializers
from .models import Movie, Actor, Genre, Comment, Group, Ticket, Country, Request

class MovieGenreSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source='name')
    value = serializers.CharField(source='display_name')

    class Meta:
        model = Genre
        fields = ['key', 'value']

class MovieIdSerializer(serializers.Serializer):
    id = serializers.CharField()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'plot', 'release_date', 'genres', 'image', 'imdb_rating']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='get_likes_count', read_only=True)
    class Meta:
        model = Comment
        fields = ['id','author', 'target', 'content', 'send_date', 'likes_count']
        extra_kwargs = {'author': {'read_only': True}, 'target': {'required': False}}



class GenreSerializer(serializers.ModelSerializer):
    items = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'display_name', 'items']

class GroupSerializer(serializers.ModelSerializer):
    items = MovieListSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
        read_only_fields = ['sender']

class CountrySerializer(serializers.ModelSerializer):
    items = MovieListSerializer(many=True)
    class Meta:
        model = Country
        fields = ['id', 'name', 'display_name', 'items']