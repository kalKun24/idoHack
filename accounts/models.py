from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    total_score = models.IntegerField(default=0, verbose_name="総合得点")