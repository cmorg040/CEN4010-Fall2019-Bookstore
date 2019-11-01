from django.db import models


# Create your models here.

class Author(models.Model):
    authorName = models.CharField(max_length=15)
    authorBio = models.TextField(default="default")
    
    def __str__(self):
        return self.authorName

class Books(models.Model):
    bookName = models.CharField(max_length=200)
    bookSummary = models.TextField(default='hello')
    bookRating = models.CharField(max_length=1, default='1') # may need to be an int
    bookPrice = models.DecimalField(max_digits=10,decimal_places=2, default=2.22)
    genre = models.CharField(max_length=20)
    cover = models.ImageField(default='default.jpg', upload_to='bookCovers')
    publisherName = models.CharField(max_length=20, default="no name")
    publisherDate = models.CharField(max_length=20, default='no date')
    # publisherDate = models.DateField()
    authorName = models.ForeignKey(Author, on_delete=models.CASCADE)

class Comment(models.Model):
    bookComment = models.TextField(default="default")
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.bookComment
