from django.contrib import admin

# Register your models here.
from .models import Author, Bookname, Booksummary

admin.site.register(Author)
admin.site.register(Bookname)
admin.site.register(Booksummary)