from django.contrib import admin
from .models import Author, Books, Comment, Review, UserBought

# # Register your models here.

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Comment)

admin.site.register(Review)
admin.site.register(UserBought)