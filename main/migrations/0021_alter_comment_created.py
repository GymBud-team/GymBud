# Generated by Django 4.1.1 on 2022-10-19 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
