#-*- coding: utf-8 -*-
from django.db import models
from grmetodos.models import *

def unisulta():
    unid = TblUnidades.objects.all()
    result_list=[]
    for i in unid:
        result_list.append("%s - %s" % (i.unidade,  i.nome))
    return result_list


def atrsulta():
    atrib = TblAtribs.objects.all()
    atr_list=[]
    for i in atrib:
        atr_list.append("%s: %s // %s" % (i.medida, i.nome,  i.descricao))
    return atr_list

def metatetssulta():
    result_list=[]
    metos=TblMetAtEts.objects.order_by('metodo').all()
    for p in metos:
        result_list.append ("%s: %s - %s %s%s // %s " %( p.metodo,  p.atributo_estacao, p.atributo,  p.valor,  p.unidade,  p.obs ) )
        
    return result_list
    
def apesulta():
    result_list=[]
    metos=TblApetrechos.objects.order_by('apetrecho').all()
    for p in metos:
        result_list.append ("%s: %s // %s" %( p.apetrecho,  p.nome,  p.descricao) )
        
    return result_list

def metsulta():
    '''métodos'''
    result_list=[]
    metos=TblMetodos.objects.order_by('metodo').all()
    for p in metos:
        result_list.append ("%s - %s - %s // %s" %( p.metodo,  p.nome, p.local,  p.obs) )
        
    return result_list

def atretssulta():
    '''Atributos da Estação'''
    result_list=[]
    metos=TblAtrEts.objects.order_by('medida').all()
    for p in metos:
        result_list.append ("%s - %s // %s" %( p.medida, p.nome,  p.descricao) )
        
    return result_list

def inssulta():
    '''carcteristicas do apetrecho'''
    result_list=[]
    metos=TblInstrumentais.objects.order_by('apetrecho').all()
    for p in metos:
        result_list.append ("%s: %s de %s%s // %s" %( p.apetrecho, p.atributo,  p.valor,  p.unidade,  p.obs) )
        
    return result_list

def metInssulta():
    '''quantidade de apetrechos por estação'''
    result_list=[]
    metos=TblMetIns.objects.order_by('metodo').all()
    for p in metos:
        result_list.append ("%s: %s - %d" %( p.metodo, p.apetrecho,  p.quantidade) )
        
    return result_list

    
    
    
    
    
    
