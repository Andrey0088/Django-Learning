from django.urls import path
#igual ao original

from .views import index, contato
#o ponto indica que é do próprio módulo core, do arquivo views, importa o arquivo/view index e contato.;

#configurando rotas:
#index e contato são views
urlpatterns = [
    path('', index),
    path('contato', contato),
]
#se for para a raiz, envia para index
#se for para contato, envia para contato

#assim tira as rotas do arquivo urls do projeto, e coloca aqui.
#tudo que for para a raiz, manda para a aplicação core, ela que vai receber essas requisições.
#toda requisição que for para a raiz, envia para a aplicação core.
