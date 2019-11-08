from django.db import models

class Book(models.Model):
    title = models.CharField('Book Title', max_length=120)
    author = models.CharField('Author', max_length=50)
    genre = models.CharField('Genre', max_length=20)
    #Note: A book could have multiple genres. Use an array?
    num_sales = models.IntegerField('Units Sold')
    rating = models.IntegerField('Rating')
    price = models.IntegerField('Price')
    release_date = models.DateField('Release Date')
    description = models.TextField(blank=True)