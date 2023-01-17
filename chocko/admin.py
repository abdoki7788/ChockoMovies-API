from django.contrib import admin
from .models import Actor, Genre, Company, Movie, Serie, Comment, Group

# Register your models here.

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Company)
admin.site.register(Movie)
admin.site.register(Serie)
admin.site.register(Comment)
admin.site.register(Group)