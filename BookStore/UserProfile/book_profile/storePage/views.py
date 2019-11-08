from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    # return response
    return HttpResponse("This is the home page")


