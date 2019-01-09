from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()