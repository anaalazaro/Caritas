# Generated by Django 5.0.6 on 2024-05-23 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_customuser_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='filial',
        ),
    ]