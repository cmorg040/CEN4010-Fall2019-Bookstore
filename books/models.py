import urllib.request

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.

class Author(models.Model):
    authorName = models.CharField(max_length=15)
    authorBio = models.TextField(default="default")

    def __str__(self):
        return self.authorName


class Books(models.Model):
    bookName = models.CharField(max_length=200)
    bookSummary = models.TextField(default='hello')
    bookRating = models.CharField(max_length=1, default='1')  # may need to be an int
    bookPrice = models.DecimalField(max_digits=10, decimal_places=2, default=2.22)
    genre = models.CharField(max_length=20)
    cover = models.ImageField(default='default.jpg', upload_to='bookCovers')
    publisherName = models.CharField(max_length=20, default="no name")
    publisherDate = models.CharField(max_length=20, default='no date')
    # publisherDate = models.DateField()
    authorName = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.bookName


class Comment(models.Model):
    userName = models.TextField(default="userName")
    datePosted = models.DateTimeField(default=datetime.now, blank=True)
    bookComment = models.TextField(default="default")
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.bookComment


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField('Nick name', max_length=30, blank=True, default='')
    bio = models.TextField(max_length=450, blank=True)

    def __str__(self):
        # get the profile not just the object
        return self.user.username


# Book_User hold the history of books purchased by users.
class UserBought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return '{} bought {}'.format(str(self.user.username), self.book.title)


class Review(models.Model):
    # get the appropriate book
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    # get the user writing the review
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # anonymous or not
    anonymous = models.BooleanField(default=False)
    # nickname or not
    nickname = models.BooleanField(default=False)

    # ratings from 1-5
    RATING_CHOICES = zip(range(1, 6), range(1, 6))
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    # date of the review
    date = models.DateField(default=datetime.now)

    # comment review
    comment = models.TextField(blank=True, null=True, max_length=700)

    def __str__(self):
        return '{} rating for {}'.format(self.rating, self.book.bookName)
