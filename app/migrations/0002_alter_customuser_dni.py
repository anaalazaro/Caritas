# Generated by Django 5.0.4 on 2024-05-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dni',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
