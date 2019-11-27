from django.shortcuts import render
from books.models import Books, Author
from django.http import HttpResponse
import operator
from django.db.models import Q, F
from django.views.generic import ListView
from django.core.exceptions import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#def index(request):
#    books = Book.objects.order_by('title')
#    context = { 'books': books }
#    return render(request, 'books/index.html', context)

items_per_page = 10

def index(request):
    book_list = Books.objects.order_by("bookName")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_title(request):

    book_list = Books.objects.order_by("bookName")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_author(request):

    book_list = Books.objects.order_by("authorName__authorName")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_price(request):

    book_list = Books.objects.order_by("bookPrice")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_rating(request):

    book_list = Books.objects.filter(bookRating__lte=3)
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_date(request):

    book_list = Books.objects.order_by("publisherDate")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_genre(request):

    book_list = Books.objects.order_by("genre")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_rating1(request):

    book_list = Books.objects.filter(bookRating__gte=1).order_by("bookRating")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_rating2(request):

    book_list = Books.objects.filter(bookRating__gte=2).order_by("bookRating")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_rating3(request):

    book_list = Books.objects.filter(bookRating__gte=3).order_by("bookRating")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_rating4(request):

    book_list = Books.objects.filter(bookRating__gte=4).order_by("bookRating")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })

def search_by_rating5(request):

    book_list = Books.objects.filter(bookRating__gte=5).order_by("bookRating")
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, items_per_page)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'search/search_base.html', { 'books': books })