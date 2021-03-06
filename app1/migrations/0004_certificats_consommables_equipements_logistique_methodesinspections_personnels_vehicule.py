# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-23 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180321_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codCer', models.CharField(max_length=30)),
                ('nomCer', models.CharField(max_length=30)),
                ('diplome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Consommables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codCons', models.IntegerField()),
                ('qrCodeCons', models.CharField(max_length=30)),
                ('dateExpirationCons', models.DateField()),
                ('planifierCons', models.CharField(max_length=30)),
                ('designationCons', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Equipements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codEqp', models.CharField(max_length=30)),
                ('qrCode', models.IntegerField()),
                ('numeroLot', models.IntegerField()),
                ('dateExpiration', models.DateField()),
                ('dateFabEqp', models.DateField()),
                ('dateFinEqp', models.DateField()),
                ('dateAchatEqp', models.DateField()),
                ('calibrationPeriodeEqp', models.IntegerField()),
                ('calibrationDateEqp', models.DateField()),
                ('dateProchaineDisponibiliteEqp', models.DateField()),
                ('emplacementEqp', models.CharField(max_length=30)),
                ('etatEqp', models.CharField(max_length=30)),
                ('dateEtatEqp', models.DateField()),
                ('designationEqp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='logistique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codLog', models.CharField(max_length=30)),
                ('periodeLog', models.IntegerField()),
                ('montantLog', models.IntegerField()),
                ('factureLog', models.IntegerField()),
                ('moyenTransport', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MethodesInspections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codMethIns', models.IntegerField()),
                ('nomMethIns', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personnels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matPer', models.CharField(max_length=30)),
                ('numCinPer', models.IntegerField()),
                ('nomPer', models.CharField(max_length=30)),
                ('prenomPer', models.CharField(max_length=30)),
                ('dateNaissancePer', models.DateField()),
                ('lieuNaissancePer', models.CharField(max_length=30)),
                ('numTelephone1Per', models.IntegerField()),
                ('adressePer', models.CharField(max_length=30)),
                ('telephoneConjoint', models.IntegerField()),
                ('fonctionPer', models.CharField(max_length=30)),
                ('dateEmbauchePer', models.DateField()),
                ('numPassportPer', models.IntegerField()),
                ('dateFinPassportPer', models.DateField()),
                ('permisConduitePer', models.CharField(max_length=30)),
                ('dateFinPermis', models.DateField()),
                ('matCNSSPer', models.CharField(max_length=30)),
                ('situationFamiliale', models.CharField(max_length=30)),
                ('nombresEnfants', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matVeh', models.CharField(max_length=30)),
                ('marqueVeh', models.CharField(max_length=30)),
                ('typeVeh', models.CharField(max_length=30)),
                ('numSerieVeh', models.IntegerField()),
                ('dateAchatVeh', models.DateField()),
            ],
        ),
    ]
