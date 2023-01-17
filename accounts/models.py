from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    profile = models.ImageField(upload_to='profiles', default='profile.png', null=True, blank=True)
    about = models.TextField(blank=True, null=True)