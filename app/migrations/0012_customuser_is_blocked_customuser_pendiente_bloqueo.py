# Generated by Django 5.0.4 on 2024-06-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_customuser_is_blocked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pendiente_bloqueo',
            field=models.BooleanField(default=False),
        ),
    ]
