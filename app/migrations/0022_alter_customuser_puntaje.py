# Generated by Django 4.2.11 on 2024-07-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_customuser_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='puntaje',
            field=models.IntegerField(default=3),
        ),
    ]
