from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    name = models.CharField(max_length=255)
    storyline = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
    