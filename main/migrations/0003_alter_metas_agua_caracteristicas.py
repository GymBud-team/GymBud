# Generated by Django 4.1 on 2022-09-23 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_metas_agua'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metas',
            name='agua',
            field=models.FloatField(choices=[(1, '1 litro'), (1.5, '1.5 litros'), (2, '2 litros'), (2.5, '2.5 litros'), (3, '3 litros')], default=0),
        ),
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField(default=0)),
                ('peso_inicial', models.IntegerField(default=0)),
                ('altura', models.FloatField(default=0)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]