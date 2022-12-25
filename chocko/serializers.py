from rest_framework import serializers
from .models import Movie, Actor

class MovieIdSerializer(serializers.Serializer):
    movie_id = serializers.CharField()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=20)
    title = serializers.CharField(max_length=50)
    fullTitle = serializers.CharField(max_length=100)
    releaseDate = serializers.CharField()
    plot = serializers.CharField()
    actorList = serializers.ListField()
    genreList = serializers.ListField()
    companyList = serializers.ListField()
    countries = serializers.CharField()
    imDbRating = serializers.CharField(max_length=4)
    image = serializers.URLField()
    trailer = serializers.URLField()
    runtimeMins = serializers.CharField()
    contentRating = serializers.CharField()

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'