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

