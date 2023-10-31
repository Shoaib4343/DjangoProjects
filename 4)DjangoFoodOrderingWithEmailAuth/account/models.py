from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    bio = models.CharField(max_length=40)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()
