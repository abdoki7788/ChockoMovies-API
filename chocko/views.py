from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieIdSerializer, MovieDetailSerializer
from utils.api_calls import get_movie_by_id

class GetMovieData(APIView):
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