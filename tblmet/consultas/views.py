#-*- coding: utf-8 -*-
from grmetodos.forms import *
from grmetodos.models import *
from grmetodos.views import *
from models import *
import csv
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
import codecs
from codecs import *

def platrbtt(request):
    a=atrsulta()
    mat = metatetssulta()
    u = unisulta()
    ape=apesulta()
    mett=TblMetodos.objects.all()
    metatets=TblMetAtEts.objects.all()
    metatrets=TblAtrEts.objects.all()
    metins=TblMetIns.objects.all()
    metapes=TblApetrechos.objects.all()
        
    return direct_to_template(request, 'outmettt.html', {
        'mett': mett, 
        'metatets':metatets,
        'metatrets':metatrets, 
        'metins':metins, 
        'metapes':metapes, 
          
        })


def platrb (request):
    a=atrsulta()
    mat = metatetssulta()
    u = unisulta()
    ape=apesulta()
    met=metsulta()
    atts=atretssulta()
    ins=inssulta()
    meins=metInssulta()
    
    return direct_to_template(request, 'outmet.html', {

        'unid':u,
        'atrib':a,
        'meto':mat,
        'ape':ape, 
        'met':met, 
        'atrest':atts, 
        'ins':ins, 
        'meins':meins, 
         
        })

def uatrsulta(request):
    global nome
    nome=atrsulta()
    return expcsv(request)

def umetatetssulta(request):
    global nome
    nome=metatetssulta()
    return expcsv(request)

def uunisulta(request):
    global nome
    nome=unisulta()
    return expcsv(request)

def uapesulta(request):
    global nome
    nome=apesulta()
    return expcsv(request)

def umetsulta(request):
    global nome
    nome=metsulta()
    return expcsv(request)

def uatretssulta(request):
    global nome
    nome=atretssulta()
    return expcsv(request)

def uinssulta(request):
    global nome
    nome=inssulta()
    return expcsv(request)

def umetinssulta(request):
    global nome
    nome=metInssulta()
    return expcsv(request)

def expcsv(request):
    response=HttpResponse(mimetype='text/csv')
    response['Content-Disposition']='attachment; filename=planotrabalho.csv'
    #nome=atrsulta()
    w=csv.writer(response,  delimiter=';')
    #ww=str(w)
    g=range(len(nome))
    #gn=unicode(nome, 'utf-8')
    def tr():
        nomed=[]
        for i in nome:
            nomed.append(i.encode("utf-8"))
        return nomed
    nom=tr()
    gh=map(None, g, nom)
    #re=[]
    for r in gh:
        w.writerow(r)

    return response
