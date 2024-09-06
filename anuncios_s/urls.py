# anuncios_s/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.novo_anuncio, name='novo_anuncio'),
    path('editar/<int:pk>/', views.editar_anuncio, name='editar_anuncio'),
    path('deletar/<int:pk>/', views.deletar_anuncio, name='deletar_anuncio'),
    path('anuncio/<int:pk>/', views.detalhes_anuncio, name='detalhes_anuncio'),
    path('meus-anuncios/', views.meus_anuncios, name='meus_anuncios'),
]
