from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Користувач'),
        ('moderator', 'Модератор'),
        ('admin', 'Адміністратор'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


class Event(models.Model):
    date = models.DateField(unique=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.date} - {self.title}"