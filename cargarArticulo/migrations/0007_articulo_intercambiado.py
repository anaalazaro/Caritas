# Generated by Django 4.2.11 on 2024-07-03 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargarArticulo', '0006_articulo_borrado'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='intercambiado',
            field=models.BooleanField(default=False),
        ),
    ]