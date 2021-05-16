from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>I AM WORKING</h1>')

# Create your views here.
