from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    contend = models.TextField()
    published_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title