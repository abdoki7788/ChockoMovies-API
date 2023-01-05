from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MovieIdSerializer, MovieDetailSerializer, MovieSerializer, GenreSerializer, CommentSerializer, GroupSerializer, TicketSerializer, CountrySerializer
from .models import Movie, Genre, Comment, Group, Ticket, Country
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly, IsAdminOrCreateOnly
from utils.api_calls import get_movie_by_id


class GetMovieData(APIView):
    def post(self, request):
        serializer = MovieIdSerializer(data=request.data)
        if serializer.is_valid():
            id = serializer.data['movie_id']
            data = get_movie_by_id(id)
            data['plot'] = data['plotLocal']
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
    filter_backends = [SearchFilter ,DjangoFilterBackend, OrderingFilter]
    search_fields = ['title', 'full_title']
    filterset_fields = ['genres', 'actors', 'countries', 'companies']
    ordering_fields = ['realease_date', 'imdb_rating']

    def get_permissions(self):
        if self.action in ['save', 'unsave', 'comments']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @action(methods=['GET', 'POST'], detail=True)
    def comments(self, request, pk):
        obj = self.get_object()
        if request.method.lower() == 'get':
            return Response(CommentSerializer(obj.comments, many=True).data)
        else:
            serialized_data = CommentSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.validated_data['author'] = request.user
                serialized_data.validated_data['target'] = obj
                serialized_data.save()
                return Response(serialized_data.data)
            else:
                return Response(serialized_data.errors)
    
    @action(methods=['post'], detail=True)
    def save(self, request, id):
        obj = self.get_object()
        obj.saves.add(request.user)
        obj.save()
        return Response({'datail': 'successfuly saved'})
    
    @action(methods=['post'], detail=True)
    def unsave(self, request, id):
        obj = self.get_object()
        obj.saves.remove(request.user)
        obj.save()
        return Response({'datail': 'successfuly unsaved'})

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GenreSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = CommentSerializer
    filterset_fields = ['target']
    ordering = ['send_date']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GroupSerializer

class TicketView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    permission_classes = [IsAdminOrCreateOnly]
    serializer_class = TicketSerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CountrySerializer