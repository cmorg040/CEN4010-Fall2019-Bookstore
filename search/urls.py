from django.urls import path
from django.conf.urls import include, url
from . import views
from search.views import *

app_name = 'search'

urlpatterns = [
    path('', views.search_by_title, name='search'),
    path('author', views.search_by_author, name='author'),
    # path('', views.search_by_author, name='search_by_author'),
]

from django.urls import path, include   # path is to create the path in urlpatterns
from . import views # Import the views defined in the current directory

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
