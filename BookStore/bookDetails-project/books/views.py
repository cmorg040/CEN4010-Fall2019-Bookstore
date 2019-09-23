from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

def details(request):
    return render(request, 'books/details.html')
