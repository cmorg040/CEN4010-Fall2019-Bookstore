from django.db import models


# Create your models here.

class Author(models.Model):
    authorName = models.CharField(max_length=15)

    def __str__(self):
        return self.authorName

class Bookname(models.Model):
    bookName = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.bookName

class Booksummary(models.Model):
    summary = models.CharField(max_length=200)
    bookname = models.ForeignKey(Bookname, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary

