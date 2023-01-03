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
    image = models.URLField()

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.display_name

class MovieType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class ContentRating(models.Model):
    rating = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.rating    

class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    full_title = models.CharField(max_length=100)
    type = models.ForeignKey(MovieType, on_delete=models.SET_NULL, null=True, related_name='items')
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
    content_rating = models.ForeignKey(ContentRating, related_name='movies', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.full_title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    target = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='liked_comments')
    send_date = models.DateTimeField(auto_now_add=True)

    def get_likes_count(self):
        return self.likes.count()
    
    def __str__(self) -> str:
        return f'{self.author.username} on {self.target.movieid} at {self.send_date}'

class Group(models.Model):
    title = models.CharField(max_length=50)
    items = models.ManyToManyField(Movie, related_name='added_groups')

    def __str__(self) -> str:
        return self.title


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'by "{self.name}" at {self.send_date}'