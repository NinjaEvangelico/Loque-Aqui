from django.urls import path
from .views import reservar_anuncio, minhas_reservas, cancelar_reserva

urlpatterns = [
    path('reservar/<int:pk>/', reservar_anuncio, name='reservar_anuncio'),
    path('minhas-reservas/', minhas_reservas, name='minhas_reservas'),
    path('cancelar-reserva/<int:pk>/', cancelar_reserva, name='cancelar_reserva'),
]
