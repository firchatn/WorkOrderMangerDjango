# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class WorkOrdre(models.Model):
	codWo = models.IntegerField()
	numeroWo= models.CharField(max_length=30)
	numeroRapportWo= models.CharField(max_length=30)
	numeroCertificatWo= models.IntegerField()
	numBCCltWo = models.IntegerField()
	dateDebutWo = models.DateField()
	dateFinWo = models.DateField()
	typeInterventionWo = models.CharField(max_length=30)
	sousTranitanceWo = models.CharField(max_length=30)
	exigenceSpecifiqueCltWo = models.CharField(max_length=30)
	exigenceHSECltWo = models.CharField(max_length=30)
	CSFWo = models.CharField(max_length=30)
	onSiteControleWo = models.CharField(max_length=30)
	liftingWo = models.CharField(max_length=30)
	def __str__(self):
 		return str("WO-DR-0"+str(self.id)+"/18")

"""
 	def __str__(self):
 		if codWo> 500:
 			return str("WO-DR-0"+str(self.id)+"/18")
 		else :
 			return str("WO-JNT-0"+str(self.id)+"/18")
"""


 		

class Personnel(models.Model):
	matPer = models.CharField(max_length=30)
	numCinPer = models.IntegerField()
	nomPer = models.CharField(max_length=30)
	prenomPer = models.CharField(max_length=30)
	dateNaissancePer =models.DateField()
	lieuNaissancePer = models.CharField(max_length=30)
	numTelephone1Per = models.IntegerField()
	adressePer = models.CharField(max_length=30)
	telephoneConjoint = models.IntegerField()
	fonctionPer = models.CharField(max_length=30)
	dateEmbauchePer = models.DateField()
	numPassportPer = models.IntegerField()
	dateFinPassportPer  = models.DateField()
	permisConduitePer  = models.CharField(max_length=30)
	dateFinPermis = models.DateField()
	matCNSSPer = models.CharField(max_length=30)
	situationFamiliale = models.CharField(max_length=30)
	nombresEnfants = models.IntegerField()
	
	def __str__(self):
		return str(self.nomPer)

class Certificat(models.Model):
	codCer = models.CharField(max_length=30)
	nomCer = models.CharField(max_length=30)
	diplome = models.CharField(max_length=30)

	def __str__(self):
		return str(self.nomCer)
		
class Equipement(models.Model):
	codEqp = models.CharField(max_length=30)
	qrCode = models.IntegerField()
	numeroLot = models.IntegerField()
	dateExpiration= models.DateField()
	dateFabEqp = models.DateField()
	dateFinEqp = models.DateField()
	dateAchatEqp = models.DateField()
	calibrationPeriodeEqp = models.IntegerField()
	calibrationDateEqp = models.DateField()
	dateProchaineDisponibiliteEqp = models.DateField()
	emplacementEqp = models.CharField(max_length=30)
	etatEqp = models.CharField(max_length=30)
	dateEtatEqp = models.DateField()
	designationEqp = models.CharField(max_length=30)
	
	def __str__(self):
		return str("WO-DR-0"+str(self.id)+"/18")
		
class vehicule(models.Model):
	matVeh = models.CharField(max_length=30)
	marqueVeh= models.CharField(max_length=30)
	typeVeh = models.CharField(max_length=30)
	numSerieVeh= models.IntegerField()
	dateAchatVeh = models.DateField()
	
	def __str__(self):
		return str(self.matVeh)

class MethodesInspection(models.Model):
	codMethIns = models.IntegerField()
	nomMethIns = models.CharField(max_length=30)
	
	def __str__(self):
		return str(self.nomMethIns)
		
class Consommable(models.Model):
	codCons = models.IntegerField()
	qrCodeCons = models.CharField(max_length=30)
	dateExpirationCons = models.DateField()
	planifierCons = models.CharField(max_length=30)
	designationCons = models.CharField(max_length=30)
	
	def __str__(self):
		return str(self.codCons)
		
class logistique(models.Model):
	codLog = models.CharField(max_length=30)
	periodeLog = models.IntegerField()
	montantLog = models.IntegerField()
	factureLog = models.IntegerField()
	moyenTransport = models.CharField(max_length=30)
	
	def __str__(self):
		return str(self.periodeLog)
		
		
		
class Client(models.Model):
	codClt = models.IntegerField()
	nomClient = models.CharField(max_length=30)
	raisonSocialClt= models.CharField(max_length=30)
	adresseClt = models.DateField()
	emailClt = models.CharField(max_length=30)
	NumTelephoneClt = models.CharField(max_length=30)
	webClt = models.CharField(max_length=30)
	secteurClt = models.CharField(max_length=30)
	serviceClt = models.CharField(max_length=30)
	
	def __str__(self):
		return str(self.nomClient)
		
		
		
class ContactsClient(models.Model):
	codCntClt = models.IntegerField()
	codClt = models.ForeignKey(Client, on_delete= models.CASCADE)
	nomCntClt = models.CharField(max_length=30)
	prenomCntClt = models.CharField(max_length=30)
	numTelephone1CntClt = models.IntegerField()
	numTelephone2CntClt = models.IntegerField()
	emailCntClt = models.EmailField()
	fonctionCntClt= models.CharField(max_length=30)
	 
	def __str__(self):
		return str(self.nomCntClt)	
	
class CertificatPersonnel(models.Model):
	codCerPer = models.IntegerField()
	codCer = models.ForeignKey(Certificat, on_delete= models.CASCADE)
	matPer = models.ForeignKey(Personnel, on_delete= models.CASCADE)
	dateObtCert = models.DateField()
	dateExpirationCert = models.DateField()
	organismePcert = models.CharField(max_length=30)
	
	def __str__(self):
		return str(self.codCerPer)

class EquipementInspecter(models.Model):
	codEqp = models.IntegerField()
	planifierEqp = models.CharField(max_length=30)
	designationEqp = models.CharField(max_length=30)

	def __str__(self):
		return str(self.codEqp)

class Site(models.Model):
	codSite = models.IntegerField()
	nomSite = models.CharField(max_length=30)
	typeSite = models.CharField(max_length=30)
	urlSite = models.CharField(max_length=30)
	
	def __str__(self):
		return str(self.nomSite)

class Service(models.Model):
	codSer = models.IntegerField()
	nomSer = models.CharField(max_length=30)
	typeSer = models.CharField(max_length=30)
		
	def __str__(self):
		return str(self.nomSer)

class WOPersonnel(models.Model):
	document = models.CharField(max_length=30)
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	matPer = models.ForeignKey(Personnel, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.document)
	
class WOEqpInspecter(models.Model):
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	codEqp = models.ForeignKey(EquipementInspecter, on_delete= models.CASCADE)
	quantite = models.CharField(max_length=30)

	def __str__(self):
		return str(self.document)

class WOConsommable(models.Model):
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	codCons = models.ForeignKey(Consommable, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.codWo)

class WOMethodeInspection(models.Model):
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	codMethIns = models.ForeignKey(MethodesInspection, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.codWo)

class WOVehicule(models.Model):
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	matVeh = models.ForeignKey(vehicule, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.codWo)

class WOEquipement(models.Model):
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	codEqp = models.ForeignKey(Equipement, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.codWo)
		
class WOLogistique(models.Model):
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	codLog = models.ForeignKey(logistique, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.codWo)

class SiteClient(models.Model):
	codSite = models.ForeignKey(Site, on_delete= models.CASCADE)
	codClt= models.ForeignKey(Client, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.codClt)

class WOService(models.Model):
	codWo = models.ForeignKey(WorkOrdre, on_delete= models.CASCADE)
	codSer = models.ForeignKey(Service, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.codWo)