from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bodyweight = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=((('male', 'male'), ('female', 'female'))))
