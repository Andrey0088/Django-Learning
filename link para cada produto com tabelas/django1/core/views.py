from django.shortcuts import render
from .models import Produto
# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programaçao Web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk) #pega o objeto pelo pk

    #variável chamada contexto
    #criou um dicionário, a chave é 'produto'
    context = {
        'produto': prod
    }
    #a chave 'produto' que permite usar o 'produto.preço', 'produto.id', 'produto.estoque' no produto.html e index.html
    
    return render(request, 'produto.html', context)
    #passa context como parametro tbm
