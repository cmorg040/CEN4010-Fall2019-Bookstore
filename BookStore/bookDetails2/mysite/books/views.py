from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader, RequestContext
from .models import Bookname


# Create your views here.

def index(request):
    books = Bookname.objects.order_by('-bookName').reverse()
    context = { 'books': books }
    return render(request, 'books/index.html', context)

def detail(request, book_id):
    book = Bookname.objects.get(pk = book_id)
    return render(request, 'books/detail.html', {'book': book})
# return HttpResponse('this is the detail view of the book: %s' % book_id)
