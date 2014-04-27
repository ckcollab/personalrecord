from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bodyweight = models.IntegerField(default=0)
