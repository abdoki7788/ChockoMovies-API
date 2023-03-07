#### imports
from rest_framework.viewsets       import ModelViewSet
from rest_framework.generics       import ListCreateAPIView
from rest_framework.decorators     import action
from rest_framework.response       import Response
from rest_framework.permissions    import IsAuthenticated
from rest_framework.filters        import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers    import MovieIdSerializer, MovieCreateSerializer, MovieDetailSerializer, GenreListSerializer, GenreSerializer, CommentSerializer, GroupSerializer, TicketSerializer, CountrySerializer, RequestSerializer, MovieListSerializer
from .models         import Movie, Genre, Comment, Group, Ticket, Country, Request, Actor, Company, Director, ContentRating, IPAddress
from .permissions    import IsAdminOrReadOnly, IsAuthorOrReadOnly, IsAdminOrCreateOnly, IsAdminOrAuthenticatedCreateOnly
from utils.api_calls import get_movie_by_id
####

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = MovieDetailSerializer
    filter_backends = [SearchFilter ,DjangoFilterBackend, OrderingFilter]
    search_fields = ['title', 'full_title']
    filterset_fields = ['genres', 'actors', 'countries', 'companies', 'content_rating', 'type']
    ordering_fields = ['realease_date', 'imdb_rating']

    def get_permissions(self):
        if self.action in ['save', 'unsave', 'comments']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'imdb_create':
            self.serializer_class = MovieIdSerializer
        elif self.action == 'list':
            self.serializer_class = MovieListSerializer
        return super().get_serializer_class(*args, **kwargs)

    def retrieve(self, request, pk):
        instance = self.get_object()
        is_visit = self.request.query_params.get('hit')
        if is_visit:
            ip_obj, created = IPAddress.objects.get_or_create(address=request.META['REMOTE_ADDR'])
            instance.hits.add(ip_obj)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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
                return Response(serialized_data.errors, status=400)
    
    @action(methods=['post'], detail=True)
    def save(self, request, pk):
        obj = self.get_object()
        obj.saves.add(request.user)
        obj.save()
        return Response({'datail': 'successfuly saved'})
    
    @action(methods=['post'], detail=True)
    def unsave(self, request, pk):
        obj = self.get_object()
        obj.saves.remove(request.user)
        obj.save()
        return Response({'datail': 'successfuly unsaved'})
    
    @action(methods=['post'], detail=False)
    def imdb_create(self, request):
        seralized_data = self.get_serializer_class()(data=request.data)
        if seralized_data.is_valid():
            response = get_movie_by_id(seralized_data.data['id'])
            if response['errorMessage']:
                err = response['errorMessage']
                return Response({'detail': f'مشکلی پیش آمده . لطفا اطلاعات وارد شده را چک کنید :{ err }'}, status=400)
            else:
                actorList = []
                genreList = []
                companyList = []
                countryList = []
                directorList = []
                for actor in response['actorList']:
                    actorList.append(Actor.objects.get_or_create(id=actor['id'], name=actor['name'], image=actor['image'])[0].id)
                for genre in response['genreList']:
                    genreList.append(Genre.objects.get_or_create(name=genre['key'], display_name=genre['value'])[0].id)
                for company in response['companyList']:
                    companyList.append(Company.objects.get_or_create(id=company['id'], name=company['name'])[0].id)
                for country in response['countryList']:
                    countryList.append(Country.objects.get_or_create(name=country['key'], display_name=country['value'])[0].id)
                for director in response['directorList']:
                    directorList.append(Director.objects.get_or_create(id=director['id'], name=director['id'])[0].id)
                movie_create_data = MovieCreateSerializer(data={
                    "id":response['id'],
                    "title":response['title'],
                    "full_title":response['fullTitle'],
                    "type":'S' if response['type']=='TVSeries' else 'M',
                    "release_date":response['releaseDate'],
                    "plot":response['plotLocal'] if response['plotLocalIsRtl'] else response['plot'],
                    "actors":actorList,
                    "genres":genreList,
                    "companies":companyList,
                    "countries":countryList,
                    "directors":directorList,
                    "imdb_rating":response['imDbRating'],
                    "votes_count":response['imDbRatingVotes'],
                    "image":response['image'],
                    "trailer":response['trailer']['linkEmbed'] if not response['trailer']['errorMessage'] else None,
                    "content_rating": ContentRating.objects.get_or_create(rating=response['contentRating'])[0].id if response['contentRating'] else None,
                    "time":response['runtimeMins'] if response['type'] == 'Movie' else None,
                    "time_string":response['runtimeStr'] if response['type'] == 'Movie' else None
                })
                if movie_create_data.is_valid():
                    movie_create_data.save()
                    return Response(movie_create_data.data)
                else:
                    return Response(movie_create_data.errors, status=400)
        else:
            return Response(seralized_data.errors, status=400)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GenreSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = GenreListSerializer
        return super().get_serializer_class()


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


class ResquestView(ListCreateAPIView):
    queryset = Request.objects.all()
    permission_classes = [IsAdminOrAuthenticatedCreateOnly]
    serializer_class = RequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['sender'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CountrySerializer
    lookup_field = 'name'