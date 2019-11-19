from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)

    avg_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.book_name


