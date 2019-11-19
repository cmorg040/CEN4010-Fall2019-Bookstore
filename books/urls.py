from django.urls import path, include
from . import views
from .views import BookListView, BookDetailView, AuthorBookListView, Review

urlpatterns = [
    path('', BookListView.as_view(), name='book-browsing'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-details'),
    path('booksPurchased/<int:id>/', views.ReviewView, name='book-details-purchased'),
    path('user/<username>', AuthorBookListView.as_view(), name='author-browsing'),
]