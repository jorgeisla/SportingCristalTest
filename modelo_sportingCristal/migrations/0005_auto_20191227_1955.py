# Generated by Django 3.0.1 on 2019-12-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo_sportingCristal', '0004_auto_20191227_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
