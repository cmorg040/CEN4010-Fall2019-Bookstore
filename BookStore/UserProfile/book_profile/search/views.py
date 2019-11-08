from django.shortcuts import render
from search.models import Book
from django.http import HttpResponse
import operator
from django.db.models import Q
from django.views.generic import ListView
from django.core.exceptions import *

#def index(request):
#    books = Book.objects.order_by('title')
#    context = { 'books': books }
#    return render(request, 'books/index.html', context)

def search(request):

    items_per_page = 10

    page_by_title = Book.objects.order_by("title")[0:items_per_page]
    # page_by_author = Book.objects.order_by("author")[0:items_per_page]

    return render(request, 'search/search_base.html', {'page': page})

# def search_by_author(request):

#     page = Book.objects.order_by("author")[0:5]

#     return render(request, 'search/search_base.html', {'page': page})