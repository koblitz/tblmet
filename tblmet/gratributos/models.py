#-*- coding: utf-8 -*-
from django.db import models

class TblAtributos(models.Model):
    tipo_valor=models.CharField(u'tipo_valor',  max_length='1')
    no_at_ca_co=models.CharField('Nome do Atributo',  max_length='40') #nome_atributo_cabecalho_coluna
    legenda=models.CharField('Legenda',  max_length='255')
    descricao=models.TextField(u'Descrição')
    referencia=models.CharField(u'Referência',  max_length='1')
    unidade_utilizada=models.CharField(u'Unidade Mensurada',  max_length='60')
    objects=models.Manager()
#    apetrecho=TbTblAtrEtslInstrumentaisManager()
    class Meta:
        db_table='tbl_atributos'

    def __unicode__(self):
        return unicode(self.no_at_ca_co)    
