from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Produto, Cliente
#importou os 2 models.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)