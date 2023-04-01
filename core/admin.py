from django.contrib import admin
from .models import Produto, Cliente


# Modo simple de registra.
# admin.site.register(Produto)
# admin.site.register(Cliente)

# Modo com Decorador
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email']
