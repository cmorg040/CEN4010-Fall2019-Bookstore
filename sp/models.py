from django.db import models

# Create your models here.
'''
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vorte = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__():
        return self.q
'''

class Author(models.Model):
    author_num = models.DecimalField(max_digits = 2, decimal_places = 2,
        primary_key=True)
    author_last = models.CharField(max_length=12)
    author_first = models.CharField(max_length=10)

class Book(models.Model):
    bookcode = models.CharField(max_length=4, primary_key=True)
    title = models.CharField(max_length=40)
    publisherCode = models.CharField(max_length=3)
    _type = models.CharField(max_length=1)
    paperback = models.CharField(max_length=1)


class Branch(models.Model):
    branch_num = models.DecimalField(max_digits = 2, decimal_places = 2,
        primary_key=True)
    branch_name = models.CharField(max_length=50)
    branch_location = models.CharField(max_length=50)
    


class Copy(models.Model):
    book_code = models.CharField(max_length=4,primary_key=True)
    #branch_num = models.DecimalField(max_digits = 2, decimal_places = 2)
    branch_num = models.ForeignKey('Branch', on_delete = models.CASCADE)
    copyNum = models.DecimalField(max_digits = 2, decimal_places = 2)
    quality = models.CharField(max_length=20)
    price = models.DecimalField(max_digits = 8, decimal_places = 8)


class Publisher(models.Model):
    publishercode = models.CharField(max_length=3, primary_key=True)
    publishername = models.CharField(max_length=25)
    city = models.CharField(max_length=20)

class Wrote(models.Model):
    #book_code = models.CharField(max_length=4, primary_key=True)
    book_code = models.ForeignKey('Copy', on_delete=models.CASCADE)
    author_num = models.DecimalField(max_digits = 2, decimal_places = 2)
    sequence = models.DecimalField(max_digits = 2, decimal_places = 2)

#class Inventory(models.Model):
