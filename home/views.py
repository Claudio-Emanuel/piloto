from django.shortcuts import HttpResponse, render
from .forms import ContatoForm, ProdutoForm
# Create your views here.
from django.http import HttpResponse


#------------Funcao de Home/Tela Inicial------------   
def index(request):
    return render(request,'index.html')


#------------Funcao nao importante------------   

def sobre(request):
    return render(request,'sobre.html')


#-----------Funcao de formulario de contato------------   
def contato(request):
    form = ContatoForm()
    contexto =  {
        'form': form,
    }
    return render(request,'contato.html',contexto)


#------------Funcao de Encher Linguica------------   
def ajuda():
    return HttpResponse("<h1>Esta eh a pagina de ajuda</h1>")

def exibir_item(request, id):
    return render(request, 'exibir_item.html',{'id':id})

def perfil(request, usuario):
    return render(request, 'perfil.html',{'str':usuario})

#------------Funcao de Dia da semana------------   
def semana(request, num):
    if num==1 :
        return render(request, 'semana.html',{"mensagem":"Domingo"})
    if num==2 :
        return render(request, 'semana.html',{"mensagem":"Segunda-Feira"})
    if num==3 :
        return render(request, 'semana.html',{"mensagem":"Terça-Feira"})
    if num==4 :
        return render(request, 'semana.html',{"mensagem":"Quarta-Feira"})
    if num==5 :
        return render(request, 'semana.html',{"mensagem":"Quinta-Feira"})
    if num==6 :
        return render(request, 'semana.html',{"mensagem":"Sexta-Feira"})
    if num==7 :
        return render(request, 'semana.html',{"mensagem":"Sabado-Feira"})
    else:
        return render(request, 'semana.html',{"mensagem":"O numero passado corresponde a um num invalido"})
    

#------------Funcao de Produto com a Lista de Produtos------------    
def produto(request):
    #dados que serao passados
    context={
        'lista': [
            {'id':1, 'nome':'Notebook','preco':'R$2.500,00'},
            {'id':2, 'nome':'Monitor','preco':'R$500,00'},
            {'id':3, 'nome':'Teclado','preco':'R$80,00'},
        ]
    }
    #Renderiza os dados
    return render(request, 'produto.html',context)


#------------Funcao de Formulario de cadastro de produto------------   
def formproduto(request):
    form= ProdutoForm()
    contexto= {
        'form':form
    }
    return render(request,'formproduto.html',contexto)

#------------Funcao dos botoes de produto------------ 
def detalhes_produto(request,id):
    return render(request)

def editar_produto(request,id):
    return render()

def excluir_produto(request,id):
    return render()