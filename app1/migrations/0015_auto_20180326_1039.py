# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-26 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20180326_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woconsommable',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
        migrations.AlterField(
            model_name='woeqpinspecter',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
        migrations.AlterField(
            model_name='woequipement',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
        migrations.AlterField(
            model_name='wologistique',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
        migrations.AlterField(
            model_name='womethodeinspection',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
        migrations.AlterField(
            model_name='wopersonnel',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
        migrations.AlterField(
            model_name='woservice',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
        migrations.AlterField(
            model_name='wovehicule',
            name='codWo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.WorkOrdre'),
        ),
    ]
