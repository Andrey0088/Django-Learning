from pdb import post_mortem
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Post  # Não esqueça de importar o modelo

def index(request):
    return render(request, 'feed.html')


def feed(request):
    posts = Post.objects.all().order_by('-date')  # Recupera todos os posts ordenados por data
    context = {
        'posts': posts
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        content = request.POST.get("content")
        # Criar e salvar um novo post no banco de dados
        post = Post(author=author, content=content)
        post.save()
        return redirect('/feed')  # Use redirect ao invés de HttpResponseRedirect para simplicidade
    else:
        return render(request, 'publicate.html')