from django.shortcuts import render
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

class BookDetailView(DetailView):
    model = Books
    
def details(request):
    return render(request, 'books/details.html')
    # return HttpResponse('<h1>Book details</h1>')

