# Generated by Django 3.0.1 on 2019-12-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo_sportingCristal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referee',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stadium',
            name='city',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stadium',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stadium',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stadium',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
