from django.db import models


# Create your models here.

class Author(models.Model):
    authorName = models.CharField(max_length=15)
    authorBio = models.TextField(default="default")
    
    def __str__(self):
        return self.authorName

class Books(models.Model):
    bookName = models.CharField(max_length=200)
    bookSummary = models.TextField
    # bookComments = models.ManyToManyField(Comment)
    bookRating = models.CharField(max_length=1, default='1') # may need to be an int
    # do i need to include book price ? 
    genre = models.CharField(max_length=20)
    cover = models.ImageField(default='default.jpg', upload_to='bookCovers')
    publisherName = models.CharField(max_length=20, default="no name")
    publisherDate = models.CharField(max_length=20, default='no date')
    # publisherDate = models.DateField()
    authorName = models.ForeignKey(Author, on_delete=models.CASCADE)

class Comment(models.Model):
    bookComment = models.TextField(default="default")
    bookName = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.bookComment