from django.db import models

#importing all models from the book details app to avoid database problems

# class Book(models.Model):
#     title = models.CharField('Book Title', max_length=120)
#     author = models.ForeignKey('Author', max_length=50)
#     genre = models.CharField('Genre', max_length=20)
#     #Note: A book could have multiple genres. Use an array?
#     num_sales = models.IntegerField('Units Sold')
#     rating = models.IntegerField('Rating')
#     price = models.IntegerField('Price')
#     release_date = models.DateField('Release Date')
#     description = models.TextField(blank=True)

# class Author(models.Model):
#     authorName = models.CharField(max_length=15)
#     authorBio = models.TextField(default="default")
    
#     def __str__(self):
#         return self.authorName

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