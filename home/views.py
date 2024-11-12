from django.shortcuts import HttpResponse 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def ajuda(request):
    return HttpResponse("<h1>Esta eh a pagina de ajuda</h1>")