from django.shortcuts import render, redirect, get_object_or_404
from .models import Anuncio
from .forms import AnuncioForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def home(request):
    anuncios = Anuncio.objects.all().order_by('-data_criacao')
    return render(request, 'anuncios_s/home.html', {'anuncios': anuncios})

#Lógica necessária para a criação de um anuncio
@login_required
def novo_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
             anuncio = form.save(commit=False)
             anuncio.usuario = request.user  # Atribui o usuário logado
             anuncio.save()
        return redirect('home')
    else:
        form = AnuncioForm()
    return render(request, 'anuncios_s/novo_anuncio.html', {'form': form})

#Lógica necessária para a edição de um anuncio ja existente
@login_required
def editar_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if anuncio.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar este anúncio.")
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnuncioForm(instance=anuncio)
    return render(request, 'anuncios_s/editar_anuncio.html', {'form': form, 'anuncio': anuncio})

#Lógica necessária para excluir anuncios
@login_required
def deletar_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if anuncio.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para excluir este anúncio.")
    if request.method == 'POST':
        anuncio.delete()
        return redirect('home')
    return render(request, 'anuncios_s/deletar_anuncio.html', {'anuncio': anuncio})
