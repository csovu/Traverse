from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    location = models.CharField(max_length=40, null=True, blank=True)
    favorites = models.CharField(max_length=500, null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.username
    