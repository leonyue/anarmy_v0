from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#https://docs.djangoproject.com/en/1.11/intro/tutorial01/
def index(request):
    return HttpResponse("Hello, World.You're at the polls index.")
