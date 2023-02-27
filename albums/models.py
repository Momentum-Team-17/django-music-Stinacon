from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
