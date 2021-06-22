from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class TaskUser(AbstractUser):
    ava = models.ImageField(upload_to='media', blank=True)
    