# Generated by Django 5.0.6 on 2024-06-12 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crearFilial', '0004_filial_turnos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filial',
            name='turnos',
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('turnos_disponibles', models.PositiveIntegerField()),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos', to='crearFilial.filial')),
            ],
            options={
                'unique_together': {('filial', 'fecha')},
            },
        ),
    ]
