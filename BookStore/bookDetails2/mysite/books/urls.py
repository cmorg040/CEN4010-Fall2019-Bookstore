from django.urls import path
from . import views
from .views import BookListView, BookDetailView, AuthorBookListView

urlpatterns = [
    path('', BookListView.as_view(), name='book-browsing'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-details'),
    path('user/<username>', AuthorBookListView.as_view(), name='author-browsing'),    
]