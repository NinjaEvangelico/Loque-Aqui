from django.db import models
from django.contrib.auth.models import User

class Anuncio(models.Model):
    TIPO_CONTRATO_CHOICES = [
        ('anual', 'Anual'),
        ('mensal', 'Mensal'),
        ('semanal', 'Semanal'),
        ('diaria', 'Diária'),
    ]

    local = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_contrato = models.CharField(max_length=10, choices=TIPO_CONTRATO_CHOICES)
    disponivel = models.BooleanField(default=True) 
    descricao = models.TextField()
    fotos = models.ImageField(upload_to='anuncios/', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.local} - {self.get_tipo_contrato_display()} - R$ {self.preco}"

    def mudar_status(self):
        self.disponivel = not self.disponivel
        self.save()