from django.shortcuts import HttpResponse 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim</h1>")

def contato(request):
    return HttpResponse("<h1>Esta eh a pagina de contato</h1>")

def ajuda(request):
    return HttpResponse("<h1>Esta eh a pagina de ajuda</h1>")