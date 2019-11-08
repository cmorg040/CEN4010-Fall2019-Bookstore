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

items_per_page = 10

def search_by_title(request):

    page_by_title = Book.objects.order_by("title")[0:items_per_page]
    # page_by_author = Book.objects.order_by("author")[0:items_per_page]

    return render(request, 'search/search_base.html', {'page': page_by_title})

def search_by_author(request):

    page_by_author = Book.objects.order_by("author")[0:items_per_page]

    return render(request, 'search/search_base.html', {'page': page_by_author})

def search_by_price(request):

    page_by_price = Book.objects.order_by("price")[0:items_per_page]

    return render(request, 'search/search_base.html', {'page': page_by_price})

def search_by_rating(request):

    page_by_rating = Book.objects.order_by("rating")[0:items_per_page]

    return render(request, 'search/search_base.html', {'page': page_by_rating})

def search_by_date(request):

    page_by_date = Book.objects.order_by("release_date")[0:items_per_page]

    return render(request, 'search/search_base.html', {'page': page_by_date})