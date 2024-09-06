from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Anuncio
from .forms import AnuncioForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import Anuncio
from reservas.models import Reserva

def home(request):
    agora = timezone.now().date()  # Data atual
    reservas = Reserva.objects.filter(data_fim__gte=agora, cancelada=False)  # Reservas futuras ou atuais
    
    # Obtém IDs dos anúncios que estão reservados
    anuncios_reservados_ids = reservas.values_list('anuncio_id', flat=True)
    
    # Filtra anúncios disponíveis (não reservados)
    anuncios_disponiveis = Anuncio.objects.filter(
        disponivel=True
    ).exclude(
        id__in=anuncios_reservados_ids
    ).order_by('-data_criacao')

    return render(request, 'anuncios_s/home.html', {'anuncios': anuncios_disponiveis})
#Lógica necessária para a criação de um anuncio
@login_required
def novo_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
             anuncio = form.save(commit=False)
             anuncio.usuario = request.user  # Atribui o usuário logado
             anuncio.save()
            #  messages.success(request, "Anúncio criado com sucesso!")
        return redirect('/')
    else:
        form = AnuncioForm()
    return render(request, 'anuncios_s/novo_anuncio.html', {'form': form})

#Lógica para exibição de detalhes do anúncio
def detalhes_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    return render(request, 'detalhes_anuncio.html', {'anuncio': anuncio})

#Lógica para exibição da lista de anuncios criados pelo usuario
def meus_anuncios(request):
    anuncios = Anuncio.objects.filter(usuario=request.user).order_by('-data_criacao')
    return render(request, 'anuncios_s/meus_anuncios.html', {'anuncios': anuncios})

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
