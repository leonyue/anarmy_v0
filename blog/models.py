from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 150,default = "empty subtitle")
    body = models.TextField()
    timestamp = models.DateTimeField()
