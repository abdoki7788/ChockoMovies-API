from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import MovieIdSerializer, MovieDetailSerializer, MovieSerializer, GenreSerializer, CommentSerializer
from .models import Movie, Genre, Comment
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from utils.api_calls import get_movie_by_id


class GetMovieData(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = MovieIdSerializer(data=request.data)
        if serializer.is_valid():
            id = serializer.data['movie_id']
            data = get_movie_by_id(id)
            data["trailer"] = data["trailer"]["link"]
            obj = MovieDetailSerializer(data=data)
            if obj.is_valid():
                return Response(obj.data)
            else:
                return Response(obj.errors)
        else:
            return Response(serializer.errors)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = MovieSerializer
    filterset_fields = ['genres', 'actors', 'country', 'companies']

    @action(methods=['GET', 'POST'], detail=True)
    def comments(self, request, pk):
        obj = self.get_object()
        if request.method.lower() == 'get':
            return Response(CommentSerializer(obj.comments, many=True).data)
        else:
            if request.user.is_authenticated:
                serialized_data = CommentSerializer(data=request.data)
                if serialized_data.is_valid():
                    serialized_data.validated_data['author'] = request.user
                    serialized_data.validated_data['target'] = obj
                    serialized_data.save()
                    return Response(serialized_data.data)
                else:
                    return Response(serialized_data.errors)

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GenreSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = CommentSerializer
    filterset_fields = ['target']