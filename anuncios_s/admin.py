
from django.contrib import admin
from .models import Anuncio

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('local', 'preco', 'tipo_contrato', 'data_criacao','disponivel')
    list_editable = ('disponivel',)
    search_fields = ('local',)
    list_filter = ('tipo_contrato', 'data_criacao')
