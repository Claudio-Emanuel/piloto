from django.shortcuts import HttpResponse ,render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Funcionou!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim</h1>")

def contato(request):
    return HttpResponse("<h1>Esta eh a pagina de contato</h1>")

def ajuda(request):
    return HttpResponse("<h1>Esta eh a pagina de ajuda</h1>")