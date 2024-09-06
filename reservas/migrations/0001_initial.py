# Generated by Django 5.1 on 2024-09-06 03:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anuncios_s', '0003_alter_anuncio_tipo_contrato'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anuncios_s.anuncio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]