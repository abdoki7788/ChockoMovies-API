from django.db import models

# Create your models here.

class Actor(models.Model):
    actorid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    image = models.URLField()

class Company(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    full_title = models.CharField(max_length=100)
    release_date = models.DateField()
    plot = models.TextField()
    actors = models.ManyToManyField(Actor, blank=True)
    genres = models.ManyToManyField(Category, blank=True)
    companies = models.ManyToManyField(Company, blank=True)
    country = models.CharField(max_length=100)
    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.URLField(blank=True)
    trailer = models.URLField(blank=True)
    time = models.IntegerField()
    content_rating = models.CharField(max_length=20, default="بدون محدودیت")