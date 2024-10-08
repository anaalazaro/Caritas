# Generated by Django 5.0.4 on 2024-05-12 01:06

import django.db.models.deletion
from Caritas import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='articulos/')),
                ('categoria', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(max_length=20)),
                ('pendiente', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
