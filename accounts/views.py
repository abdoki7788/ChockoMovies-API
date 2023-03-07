#### imports
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from djoser.views import UserViewSet

from .permissions import IsCurrentUserOrAdmin
from chocko.serializers import MovieListSerializer, CommentSerializer
####

class CustomUserViewSet(UserViewSet):

    def get_permissions(self):
        if self.action == 'saved_movies':
            self.permission_classes = [IsCurrentUserOrAdmin]
        elif self.action in ['my_saved_movies', 'my_comments']:
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