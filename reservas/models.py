from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    anuncio = models.ForeignKey('anuncios_s.Anuncio', on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(default=timezone.now)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    cancelada = models.BooleanField(default=False)

    def __str__(self):
        return f'Reserva de {self.usuario.username} para {self.anuncio.local} de {self.data_inicio} a {self.data_fim}'
