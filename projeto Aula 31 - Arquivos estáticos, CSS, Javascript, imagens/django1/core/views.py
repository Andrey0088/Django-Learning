from django.shortcuts import get_object_or_404, render
# get_object_or_404: busca um objeto ou retorna 404(página não encontrada)
#erro 500 é erro de processamento

from .models import Produto
# Create your views here.
from django.shortcuts import get_list_or_404 
from django.http import HttpResponse
from django.template import loader

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
    # prod = Produto.objects.get(id=pk) #pega o objeto pelo pk
    prod = get_object_or_404(Produto, id=pk) #traz um objeto do tipo Produto, que tem o id sendo igual à pk.
    

    #variável chamada contexto
    #criou um dicionário, a chave é 'produto'
    context = {
        'produto': prod
    }
    #a chave 'produto' que permite usar o 'produto.preço', 'produto.id', 'produto.estoque' no produto.html e index.html
    #n ao está dando certo, está gerando um erro 500, um erro de processamento

    return render(request, 'produto.html', context)
    #passa context como parametro tbm

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

#debug true -> error404
def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
#debug false -> error500

# Estamos conseguindo tratar o erro em modo de produção, nao em desenvolvimento, isso que importa; estamos mostrando a página adqueada, ao colocar uma pk inválida