# Generated by Django 5.0.4 on 2024-05-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargarArticulo', '0002_rename_categoria_articulo_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
    ]
