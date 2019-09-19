from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField('Nick Name', max_length=25, blank=True, default='')
    bio = models.TextField(max_length=500, blank=True)
