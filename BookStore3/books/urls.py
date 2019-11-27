from django.urls import path
from . import views
from .views import BookDetailView, AuthorBookListView

urlpatterns = [
    # path('', BookListView.as_view(), name='book-browsing'),
    path('', views.index, name='book-browsing'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-details'),
    path('user/<username>', AuthorBookListView.as_view(), name='author-browsing'),  
    path('booksPurchased/<int:id>/', views.ReviewView, name='book-details-purchased'),  
]