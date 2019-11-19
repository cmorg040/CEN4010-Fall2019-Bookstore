from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.template import loader, RequestContext
from django.contrib.contenttypes.models import ContentType

from books.forms import RevForm
from .models import Books, Author, Comment, Review, Profile, UserBought

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

def ReviewView(request, id):
    user = request.user
    book = get_object_or_404(Books, id=id)
    reviews = Review.objects.filter(book=book).order_by('-id')
    average_rating = reviews.aggregate(average=Avg('rating'))
    if user.is_authenticated:
        this_user_review = reviews.filter(writer=user)
        reviews_minus_this_user = reviews.exclude(writer=user)
        purchased = UserBought.objects.filter(book=book, user=user).exists()
        reviewed_already = Review.objects.filter(book=book, writer=user).exists()
    else:
        this_user_review = None
        reviews_minus_this_user = reviews
        review_form = RevForm(request.POST or None)
        purchased = None
        reviewed_already = None

    if request.method == 'POST':
        if Review.objects.filter(book=book, writer=user).exists():
            messages.warning(request, "You can only review a book once.")
            review_form = RevForm(request.POST or None)
        else:
            review_form = RevForm(request.POST or None)
            if review_form.is_valid():
                content = request.POST.get('comment')
                rating = request.POST.get('rating')
                review = Review.objects.create(book=book, writer=user, comment=content, rating=rating)
                review.save()
                messages.success(request, "You've successfully reviewed this book.")
                review_form = RevForm()
            else:
                review_form = RevForm()
    else:
        review_form = RevForm()

    context = {
        'title': 'Reviews',
        'reviews': reviews,
        'this_user_review': this_user_review,
        'reviews_minus_this_user': reviews_minus_this_user,
        'review_form': review_form,
        'book_title': book.bookName,
        'average_rating': average_rating['average'],
        'user': user,
        'purchased': purchased,
        'reviewed_already': reviewed_already,
    }
    return render(request, 'books/books_detail_purchased.html', context)

