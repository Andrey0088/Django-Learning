from django.urls import path
#igual ao original

from .views import index, contato, produto
#o ponto indica que é do próprio módulo core, do arquivo views, importa o arquivo/view index e contato.;

#configurando rotas:
#index e contato são views
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produtoName'),
    #envia um inteiro, a rota chama produto, e envia para o índice "produto"
    #criou uma rota para produto/ , que tbm tem um parâmetro(o produto com o pk), e isso vai ser passado para a view produto, e na view produto vai receber o parâmetro request e um parãmetro extra(o pk)
]
#se for para a raiz, envia para index
#se for para contato, envia para contato

#assim tira as rotas do arquivo urls do projeto, e coloca aqui.
#tudo que for para a raiz, manda para a aplicação core, ela que vai receber essas requisições.
#toda requisição que for para a raiz, envia para a aplicação core.
