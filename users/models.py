from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField('Nick name', max_length=30, blank=True, default='')
    bio = models.TextField(max_length=450, blank=True)

    def __str__(self):
        # get the profile not just the object
        return self.user.username

