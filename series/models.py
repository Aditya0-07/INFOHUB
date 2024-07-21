from django.conf import settings
from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

class Series(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')
    information = models.TextField()
    plot = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='series')
    trailer = models.FileField(upload_to='trailers/')
    available_platforms = models.CharField(max_length=200)
    platform_url = models.URLField(default='soohan.uni')
    platform_icon = models.ImageField(upload_to='icons/',  default='allinall/static/images/Bad Boys Poster.jpeg')

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='series_reviews')
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
