# Generated by Django 3.0.1 on 2019-12-27 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo_sportingCristal', '0006_auto_20191227_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='dateTime',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='timeStamp',
            new_name='timestamp',
        ),
    ]
