# Generated by Django 4.1.1 on 2022-10-01 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_ingestao'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingestao',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
