from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reserva
from .forms import ReservaForm 
from anuncios_s.models import Anuncio

@login_required
def reservar_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Verifique se o anúncio ainda está disponível
            if not anuncio.disponivel:
                return redirect('home')  # ou exiba uma mensagem de erro
            
            # Criar a reserva
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.anuncio = anuncio
            reserva.save()
            
            # Alterar o status do anúncio para indisponível
            anuncio.mudar_status()
            
            return redirect('minhas_reservas')
        else:
            # Adicionar um print ou log para depuração
            print(form.errors)  # Adicione isto para depuração
    else:
        form = ReservaForm()
    
    return render(request, 'reservas/reservar_anuncio.html', {'anuncio': anuncio, 'form': form})
    

#Mostrar as reservas do usuario 
@login_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user, cancelada=False)
    return render(request, 'reservas/minhas_reservas.html', {'reservas': reservas})

#Cancelar reserva
def cancelar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.user == reserva.usuario:
        reserva.cancelada = True
        reserva.save()
        anuncio = reserva.anuncio       
        # Alterar o status do anúncio para disponível
        if not reserva.cancelada:
            anuncio.mudar_status()  # Disponível quando a reserva é cancelada
        else:
            anuncio.mudar_status()  # Mantenha disponível se já estava cancelada
        
    return redirect('minhas_reservas')