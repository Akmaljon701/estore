from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Users"

