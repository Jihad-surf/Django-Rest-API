from django.contrib import admin
from surfstore.models import Praia, Prancha, Cliente,Compra


class Pranchas(admin.ModelAdmin):
    list_display = ('id','nome', 'preco', 'nivel_surfista')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Prancha, Pranchas)

class Praias(admin.ModelAdmin):
    list_display = ('id','nome', 'distancia_sp', 'tipo_onda')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Praia, Praias)

class Clientes(admin.ModelAdmin):
    list_display = ('id','nome','telefone','praia')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)

class Compras(admin.ModelAdmin):
    list_display = ('id','cliente','prancha','data_compra')
    list_display_links = ('id', 'cliente')
    search_fields = ('cliente',)
    list_per_page = 20

admin.site.register(Compra, Compras)
