# Generated by Django 5.0.4 on 2024-06-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_customuser_is_blocked_customuser_pendiente_bloqueo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='motivo_bloqueo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]