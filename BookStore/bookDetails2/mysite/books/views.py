from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.template import loader, RequestContext
from .models import Books, Author

# books = [ # post
#     {
#         'bookName': 'bookname',
#         'author': 'authorname',
#         'ratings': 'ratings',
#         'summary': 'summary',
#         'bookCover': 'bookCover',
#         'authorBio': 'authorBio',
#         'genre': 'genre',
#         'publishingInfo': 'publishingInfo',
#         'comments': 'comments'
#     },
#     {
#         'bookName': 'bookname',
#         'author': 'authorname',
#         'ratings': 'ratings',
#         'summary': 'summary',
#         'bookCover': 'bookCover',
#         'authorBio': 'authorBio',
#         'genre': 'genre',
#         'publishingInfo': 'publishingInfo',
#         'comments': 'comments'
#     },
# ]
# Create your views here.

def browsing(request):
    context = {
        'books': Books.objects.all()
    }
    return render(request, 'books/browsing.html', context)
    # return HttpResponse('<h1>Book Browsing page</h1>')

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
    
def details(request):
    return render(request, 'books/details.html')
    # return HttpResponse('<h1>Book details</h1>')

