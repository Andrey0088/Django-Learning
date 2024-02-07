from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500 #configurar para o 404 e para o 500
from core import views

urlpatterns = [    
    path('admin', admin.site.urls),
    path('painel/', admin.site.urls),
    path('', include('core.urls')),
#tudo que for para a raiz, manda para a aplicação core, ela que vai receber essas requisições.
]

handler404 = views.error404
#faz com que o error404 receba uma view, na dentro do core views chamada error404
handler500 = views.error500