from django.contrib import admin
from .models import Author, Books, Comment, Profile, Review, User_Bought

# # Register your models here.

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Comment)

admin.site.register(Profile)



admin.site.register(Review)
admin.site.register(User_Bought)
