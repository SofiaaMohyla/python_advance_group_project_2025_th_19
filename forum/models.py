from django.db import models
from django.conf import settings

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Massage(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)