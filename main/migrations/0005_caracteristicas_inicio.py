# Generated by Django 4.1.1 on 2022-09-26 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_caracteristicas_peso_inicial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteristicas',
            name='inicio',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]