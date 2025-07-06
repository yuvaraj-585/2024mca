from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.templates import loader


def home(request):
    temp=loader.get_template('index.html')
    return HttpResponse("Hello, Django!")
