from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    path('movie-detail', views.GetMovieData.as_view()),
]

urlpatterns += router.urls