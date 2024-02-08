from django.shortcuts import redirect, render
from .models import User

def cadastro_page(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')

        
        usuario = User()
        usuario.nome = nome
        usuario.pais = pais
        usuario.estado = estado
        usuario.cidade = cidade
        usuario.save()
        return redirect('consulta')

    else:        
        return render(request, 'cadastro.html')


def consulta_page(request):
    dados = User.objects.all()
    print(dados)
    return render(request, 'consulta.html', {'User': dados})