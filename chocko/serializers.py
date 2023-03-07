#### imports
from rest_framework import serializers

from accounts.serializers import CurrentUserSerializer
from .models import Movie, Actor, Genre, Comment, Group, Ticket, Country, Request, Company
####

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='get_likes_count', read_only=True)
    author = CurrentUserSerializer()
    class Meta:
        model = Comment
        fields = ['id','author', 'target', 'content', 'send_date', 'likes_count']
        extra_kwargs = {'author': {'read_only': True}, 'target': {'required': False}}

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'display_name', 'slug']

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
    class Meta:
        model = Country
        fields = ['id', 'name', 'display_name', 'items']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class MovieIdSerializer(serializers.Serializer):
    id = serializers.CharField()

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreListSerializer(many=True)
    type = serializers.CharField(source='get_type_display')
    class Meta:
        model = Movie
        fields = ['id', 'title', 'plot', 'release_date', 'genres', 'image', 'imdb_rating', 'type']

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreListSerializer(many=True)
    companies = CompanySerializer(many=True)
    countries = CountrySerializer(many=True)
    type = serializers.CharField(source='get_type_display')
    saves_count = serializers.IntegerField(source='saves.count')
    hits_count = serializers.IntegerField(source='hits.count')
    class Meta:
        model = Movie
        fields = ["id", "title", "full_title", "type", "release_date", "plot", "imdb_rating", "votes_count", "image", "trailer", "time", "time_string", "content_rating", "actors", "genres", "companies", "countries", "directors", "saves_count", "hits_count"]

class GroupSerializer(serializers.ModelSerializer):
    items = MovieListSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'

class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'items')


class GenreSerializer(serializers.ModelSerializer):
    items = MovieListSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'display_name', 'items']