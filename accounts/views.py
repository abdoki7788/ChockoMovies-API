#### imports
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from djoser.views import UserViewSet

from .permissions import IsCurrentUserOrAdmin
from .serializers import DashBoardSerializer
from chocko.serializers import MovieListSerializer, CommentSerializer
####

class CustomUserViewSet(UserViewSet):

    def get_permissions(self):
        if self.action == 'saved_movies':
            self.permission_classes = [IsCurrentUserOrAdmin]
        elif self.action in ['my_saved_movies', 'my_comments', 'dashboard']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @action(methods=['get'], detail=True)
    def saved_movies(self, request, id):
        obj = self.get_object()
        serialized_data = MovieListSerializer(obj.saved_movies, many=True)
        return Response(serialized_data.data)
    
    @action(methods=['get'], detail=False, url_path='me/saved_movies')
    def my_saved_movies(self, request):
        obj = request.user.saved_movies
        serialized_data = MovieListSerializer(obj, many=True)
        return Response(serialized_data.data)
    
    @action(methods=['get'], detail=False, url_path='me/comments')
    def my_comments(self, request):
        obj = request.user.comments
        serialized_data = CommentSerializer(obj, many=True)
        return Response(serialized_data.data)

    @action(methods=['get'], detail=False)
    def dashboard(self, request):
        obj = request.user
        serialized_data = DashBoardSerializer(data={
            "comments_count": obj.comments.count(),
            "requested_movies": obj.requested_movies.count(),
            "saves_count": obj.saved_movies.count(),
            "ip": request.META.get('REMOTE_ADDR'),
            "registered_date": obj.date_joined,
            "last_login_date": obj.last_login,
            "last_comments": CommentSerializer(obj.comments.latest('send_date')).data if obj.comments.order_by('send_date') else None
        })
        if serialized_data.is_valid():
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=400)