from django.contrib import admin
from .models import Actor, Category, Company, Movie

# Register your models here.

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Movie)