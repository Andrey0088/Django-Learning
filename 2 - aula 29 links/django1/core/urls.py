from django.urls import path
#igual ao original

from .views import index, contato, produto
#o ponto indica que é do próprio módulo core, do arquivo views, importa o arquivo/view index e contato.;

#configurando rotas:
#index e contato são views
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    #envia um inteiro, a rota chama produto, e envia para o índice "produto"
]
#se for para a raiz, envia para index
#se for para contato, envia para contato

#assim tira as rotas do arquivo urls do projeto, e coloca aqui.
#tudo que for para a raiz, manda para a aplicação core, ela que vai receber essas requisições.
#toda requisição que for para a raiz, envia para a aplicação core.
