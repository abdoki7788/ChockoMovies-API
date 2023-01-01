from django.db import models
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your models here.

class Actor(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    summary = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    image = models.URLField()

class Company(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    full_title = models.CharField(max_length=100)
    release_date = models.DateField()
    plot = models.TextField()
    actors = models.ManyToManyField(Actor, blank=True, related_name='works')
    genres = models.ManyToManyField(Genre, blank=True, related_name='items')
    companies = models.ManyToManyField(Company, blank=True, related_name='works')
    country = models.CharField(max_length=100)
    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.URLField(blank=True)
    trailer = models.URLField(blank=True)
    time = models.IntegerField()
    content_rating = models.CharField(max_length=20, default="بدون محدودیت")

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='liked_comments')
    send_date = models.DateTimeField(auto_now_add=True)

    def get_likes_count(self):
        return self.likes.count()