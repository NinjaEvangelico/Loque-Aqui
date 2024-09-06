# reservas/admin.py
from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'anuncio', 'data_reserva', 'data_inicio', 'data_fim')
    list_filter = ('usuario', 'anuncio', 'data_reserva')
    search_fields = ('usuario__username', 'anuncio__local')
    date_hierarchy = 'data_reserva'
