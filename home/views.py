from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def sobre(request):
    return HttpResponse("Sobre o Sistema!")

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("A view index funcionou,wow!")