from django.db import models
from django.conf import settings

# Create your models here.

class Portfolio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    media = models.FileField(upload_to="media/",blank=True,null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="likes_db")