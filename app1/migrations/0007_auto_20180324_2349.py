# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-24 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_clients_nomclient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certificats',
            new_name='Certificat',
        ),
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Consommables',
            new_name='Consommable',
        ),
        migrations.RenameModel(
            old_name='ContactsClients',
            new_name='ContactsClient',
        ),
        migrations.RenameModel(
            old_name='Equipements',
            new_name='Equipement',
        ),
        migrations.RenameModel(
            old_name='MethodesInspections',
            new_name='MethodesInspection',
        ),
        migrations.RenameModel(
            old_name='Personnels',
            new_name='Personnel',
        ),
    ]
