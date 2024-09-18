from django.contrib import admin
from rotas.models import Ambiente, Rota


class Ambientes(admin.ModelAdmin):
    list_display = ('id', 'ambiente', 'adicionado', 'ativo')
    list_display_links = ('id', 'ambiente')
    list_per_page = 10
    search_fields = ('ambiente',)
    ordering = ('id',)

admin.site.register(Ambiente, Ambientes)

class Rotas(admin.ModelAdmin):
    list_display = ('id', 'origem', 'destino', 'adicionado', 'ativo')
    list_display_links = ('id',)
    list_per_page = 10
    search_fields = ('id',)
    ordering = ('id',)

admin.site.register(Rota, Rotas)
