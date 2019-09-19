from django.urls import path, include   # path is to create the path in urlpatterns
from . import views # Import the views defined in the current directory

# Name of the app needed for the namespace on urls.py
app_name = 'settings'

urlpatterns = [
    path('', views.index, name='settings-home'),
]

