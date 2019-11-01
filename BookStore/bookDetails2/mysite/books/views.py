from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.template import loader, RequestContext
from django.contrib.contenttypes.models import ContentType
from .models import Books, Author, Comment

class BookListView(ListView):
    model = Books
    template_name = 'books/browsing.html'
    context_object_name = 'books'

class AuthorBookListView(ListView):
    model = Books
    template_name = 'books/author_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Books.objects.filter(authorName__authorName=self.kwargs.get('username'))

class BookDetailView(DetailView):
    model = Books