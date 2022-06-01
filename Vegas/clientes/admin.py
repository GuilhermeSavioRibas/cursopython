from django.contrib import admin
from .models import Cliente
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'endereco', 'bairro', 'descricao')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('bairro',)
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'endereco', 'bairro')


admin.site.register(Cliente, ClienteAdmin)
