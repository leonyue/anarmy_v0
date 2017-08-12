from django.db import models
from django.utils import timezone

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 150,default = "empty subtitle")
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
