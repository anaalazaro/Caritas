# Generated by Django 4.2.11 on 2024-07-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_customuser_puntaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='borrado',
            field=models.BooleanField(default=False),
        ),
    ]
