# Generated by Django 4.1.1 on 2022-09-26 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_metas_agua_caracteristicas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristicas',
            name='peso_inicial',
        ),
        migrations.AddField(
            model_name='caracteristicas',
            name='peso_atual',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='metas',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='PesoHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
