from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Lastrating = models.CharField(max_length=200)
    R = models.CharField(max_length=50000)


class Movies(models.Model):
    Imdb_id = models.CharField(max_length=50)
    Title = models.CharField(max_length=200)
    Poster_path = models.CharField(max_length=500)
