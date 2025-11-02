from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.TextField()
    password = models.TextField()

