from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Користувач'),
        ('moderator', 'Модератор'),
        ('admin', 'Адміністратор'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.TimeField(default="23:59")
    location = models.CharField(max_length=255, default="Не вказано")
    description = models.TextField()
    organizer = models.CharField(max_length=100, blank=True)
    event_type = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})