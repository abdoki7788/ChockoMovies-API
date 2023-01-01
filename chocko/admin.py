from django.contrib import admin
from .models import Actor, Genre, Company, Movie, Comment

# Register your models here.

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Company)
admin.site.register(Movie)
admin.site.register(Comment)