# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-21 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_necessairyexpendable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='necessairyexpendable',
            name='lot',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='necessairyexpendable',
            name='quantite',
            field=models.IntegerField(),
        ),
    ]
