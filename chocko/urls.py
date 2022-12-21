from django.urls import path
from . import views

urlpatterns = [
    path('movie-detail', views.GetMovieData.as_view())
]