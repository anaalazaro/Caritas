# Generated by Django 4.2.11 on 2024-07-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargarArticulo', '0004_alter_articulo_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='motivo_rechazo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
