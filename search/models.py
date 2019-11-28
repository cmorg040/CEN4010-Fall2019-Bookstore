from django.db import models

#importing all models from the book details app to avoid database problems

# class Books(models.Model):
#     bookName = models.CharField(max_length=200)
#     bookSummary = models.TextField(default='hello')
#     bookRating = models.CharField(max_length=1, default='1') # may need to be an int
#     bookPrice = models.DecimalField(max_digits=10,decimal_places=2, default=2.22)
#     genre = models.CharField(max_length=20)
#     cover = models.ImageField(default='default.jpg', upload_to='bookCovers')
#     publisherName = models.CharField(max_length=20, default="no name")
#     publisherDate = models.CharField(max_length=20, default='no date')
#     authorName = models.ForeignKey(Author, on_delete=models.CASCADE)
#     bookSales = models.IntegerField('Units Sold', default=0)