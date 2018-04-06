# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import  WorkOrdre,Personnel,Certificat,Equipement,vehicule,MethodesInspection,Consommable,logistique,Client,ContactsClient,CertificatPersonnel,EquipementInspecter,Site,Service,WOPersonnel,WOEqpInspecter,WOConsommable,WOMethodeInspection,WOVehicule,WOEquipement,WOLogistique,SiteClient,WOService

# Register your models here.
admin.site.register(WorkOrdre)
admin.site.register(Personnel)
admin.site.register(Certificat)
admin.site.register(Equipement)
admin.site.register(vehicule)
admin.site.register(MethodesInspection)
admin.site.register(Consommable)
admin.site.register(logistique)
admin.site.register(Client)
admin.site.register(ContactsClient)
admin.site.register(CertificatPersonnel)
admin.site.register(EquipementInspecter)
admin.site.register(Site)
admin.site.register(Service)
admin.site.register(WOPersonnel)
admin.site.register(WOEqpInspecter)
admin.site.register(WOConsommable)
admin.site.register(WOMethodeInspection)
admin.site.register(WOVehicule)
admin.site.register(WOEquipement)
admin.site.register(WOLogistique)
admin.site.register(SiteClient)
admin.site.register(WOService)



