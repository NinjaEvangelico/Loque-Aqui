# Generated by Django 5.1 on 2024-09-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios_s', '0002_anuncio_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='tipo_contrato',
            field=models.CharField(choices=[('anual', 'Anual'), ('mensal', 'Mensal'), ('semanal', 'Semanal'), ('diaria', 'Diária')], max_length=10),
        ),
    ]
