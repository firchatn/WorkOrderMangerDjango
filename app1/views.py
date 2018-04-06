# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Client
from .models import MethodesInspection
from .models import Personnel
from .models import Equipement
from .models import Consommable
from .models import EquipementInspecter
from .models import WorkOrdre
from .models import Site
from .models import Service
from .models import Certificat


# Create your views here.
def index(request):
	clt = Client.objects.all() #commantaire :instance table client
	meins = MethodesInspection.objects.all()#instance table methodes inspections
	pr = Personnel.objects.all()#instance table personnel
	eq = Equipement.objects.all()#instance table equipements
	Con = Consommable.objects.all()#instance table consommable
	wo = WorkOrdre.objects.all()#instance table work order
	eqi= EquipementInspecter.objects.all()#instance table equipements
	st = Site.objects.all()#instance table site
	sr = Service.objects.all()#instance table service
	ct = Certificat.objects.all()#instance table  certificat
	return render(request,'home.html', {"sr" : sr , "clt" : clt , "meins" : meins ,
	 "pr" : pr , "eq" : eq , "Con" : Con, "wo" :wo , "eqi" : eqi , "st" : st , "sr ": sr,"ct" : ct})

	