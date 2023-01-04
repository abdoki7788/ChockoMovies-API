from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'groups', views.CountryViewSet)


urlpatterns = [
    path('movie-detail/', views.GetMovieData.as_view(), name='movie-detail'),
    path('tickets/', views.TicketView.as_view(), name='tickets'),
]

urlpatterns += router.urls