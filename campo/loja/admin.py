from django.contrib import admin
from .models import Produto, Fornecedor
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor)