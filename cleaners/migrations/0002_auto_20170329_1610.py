# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-29 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('cleaners', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cleaner',
            options={'verbose_name': 'cleaner', 'verbose_name_plural': 'cleaners'},
        ),
        migrations.AddField(
            model_name='cleaner',
            name='city',
            field=models.ManyToManyField(to='cities.City', verbose_name='city'),
        ),
    ]
