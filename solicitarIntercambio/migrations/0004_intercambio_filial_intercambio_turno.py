# Generated by Django 5.0.6 on 2024-06-12 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crearFilial', '0004_filial_turnos'),
        ('solicitarIntercambio', '0003_rename_codigo_intercambio_intercambio_codigo_intercambio_destinatario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intercambio',
            name='filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crearFilial.filial'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='turno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
