from rest_framework import serializers
from .models import Movie, Actor, Genre, Comment, Group, Ticket, Country

class MovieGenreSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source='name')
    value = serializers.CharField(source='display_name')

    class Meta:
        model = Genre
        fields = ['key', 'value']

class MovieIdSerializer(serializers.Serializer):
    movie_id = serializers.CharField()

class MovieSerializer(serializers.ModelSerializer):
    genres = MovieGenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
    
    def save(self, **kwargs):
        genres = self.validated_data['genres']
        genre_list = []
        for genre in genres:
            try:
                obj = Genre.objects.get(**dict(genre))
            except Genre.DoesNotExist:
                obj = Genre.objects.create(**dict(genre))
            genre_list.append(obj)
        self.validated_data['genres'] = genre_list
        return super().save(**kwargs)

class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['movieid', 'title', 'release_date', 'genres', 'image', 'imdb_rating']

class MovieDetailSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=20)
    title = serializers.CharField(max_length=50)
    fullTitle = serializers.CharField(max_length=100)
    releaseDate = serializers.CharField()
    plot = serializers.CharField()
    actorList = serializers.ListField()
    genreList = serializers.ListField()
    companyList = serializers.ListField()
    countryList = serializers.ListField()
    imDbRating = serializers.CharField(max_length=4)
    image = serializers.URLField()
    trailer = serializers.URLField()
    runtimeMins = serializers.CharField()
    contentRating = serializers.CharField()

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

class CountrySerializer(serializers.ModelSerializer):
    items = MovieListSerializer(many=True)
    class Meta:
        model = Country
        fields = ['id', 'name', 'display_name', 'items']