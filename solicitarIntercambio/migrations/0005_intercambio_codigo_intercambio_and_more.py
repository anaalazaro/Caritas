# Generated by Django 5.0.6 on 2024-06-27 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crearFilial', '0008_merge_20240619_1107'),
        ('solicitarIntercambio', '0004_intercambio_filial_intercambio_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='intercambio',
            name='codigo_intercambio',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='intercambio',
            name='turno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crearFilial.turno'),
        ),
    ]
