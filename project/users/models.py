from django.contrib.auth.models import AbstractUser
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    region = models.CharField(max_length=50, null=True)

