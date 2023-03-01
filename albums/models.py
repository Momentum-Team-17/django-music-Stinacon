from django.db import models

# Create your models here.


class Album(models.Model):
    # Our Album class is inheriting from Django's Model class located in Django's models directory
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, blank=True, null=True)
    favorite_song = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
