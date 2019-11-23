from django.urls import path
from django.conf.urls import include, url
from . import views
from .views import *

app_name = 'search'

urlpatterns = [
    path('', views.search_by_title, name='search'),
    path('title', views.search_by_title, name='title'),
    path('author', views.search_by_author, name='author'),
    path('price', views.search_by_price, name='price'),
    path('rating', views.search_by_rating, name='rating'),
    path('date', views.search_by_date, name='date'),
    path('genre', views.search_by_genre, name='genre'),
    path('rating>=1', views.search_by_rating1, name='rating1'),
    path('rating>=2', views.search_by_rating2, name='rating2'),
    path('rating>=3', views.search_by_rating3, name='rating3'),
    path('rating>=4', views.search_by_rating4, name='rating4'),
    path('rating>=5', views.search_by_rating5, name='rating5'),
    # path('', views.search_by_author, name='search_by_author'),
]

# from django.urls import path, include   # path is to create the path in urlpatterns
# from . import views # Import the views defined in the current directory

# Name of the app needed for the namespace on urls.py
# app_name = 'settings'

# # all settings urls!!!
# urlpatterns = [
#     path('', views.settingsHome, name='settings-home'),
#     path('profile/', views.profile, name='profile-settings'),
#     path('account/', views.accountSettings, name='account-settings'),
#     path('billing/', views.billingSettings, name='billing-settings'),
#     path('billing/address/new/', views.addAddress, name='add-address'),
#     path('billing/address/<slug:address_slug>/', views.addressChange, name='edit-address'),
#     path('billing/creditcard/new/', views.addCreditCard, name='add-creditcard'),
#     path('billing/creditcard/<slug:creditcard_slug>/', views.creditCardChange, name='edit-creditcard'),
#     path('security/', views.securitySettings, name='security-settings')
# ]
