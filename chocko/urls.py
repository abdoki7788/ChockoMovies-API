from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'movie', views.MovieViewSet)


urlpatterns = [
    path('movie-detail', views.GetMovieData.as_view()),
]

urlpatterns += router.urls