#-*- coding: utf-8 -*-
from django.db import models


class TblUnidadesManager(models.Manager):
  
    def sulta(self):
         result_list=[]
         
         for p in TblUnidades.objects.order_by('id').all():
             
             result_list.append("%d - %s - %s - %s" %( p.id,  p.unidade, p.nome, p.descricao ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblUnidades.objects.all():
            result_id.append("%d" % p.id)
         return result_id
#        c=TblUnidades.objects.all()
#        la=[p.unidade for p in c]
#        lb=[p.nome for p in c]
#        lc=[p.descricao for p in c]
       
#        result_list=[]
#        for e, i in enumerate (la):
#            for ee, ii in enumerate (lb):
#                for eee, iii in enumerate (lc):
#                    if e==ee==eee:
#                            result_list.append("%s - %s - %s" %(i, ii, iii))

#        from django.db import connection
#        cursor = connection.cursor()
#        cursor.execute("""
#            SELECT %s
#            FROM tbl_unidades""" % args)
#        result_list=[]
#        for row in cursor.fetchall():
#           result_list.append(row)
     
 #       return result_list
    
class TblAtribsManager(models.Manager):
    def sulta(self):
         result_list=[]
         for p in TblAtribs.objects.all():
             result_list.append("%d - %s - %s - %s" %( p.id,  p.medida, p.nome, p.descricao ) )

         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblAtribs.objects.all():
            result_id.append("%d" % p.id)
         return result_id
    
class TblLocaisManager(models.Manager):
    def sulta(self):
         result_list=[]
         
         for p in TblLocais.objects.order_by('id').all():
             result_list.append("%d - %s - %s" %( p.id,  p.local, p.descricao) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblLocais.objects.order_by('id').all():
            result_id.append("%d" % p.id)
         return result_id

class TblApetrechosManager(models.Manager):
    def sulta(self):
         result_list=[]
         
         for p in TblApetrechos.objects.order_by('id').all():
             result_list.append("%d - %s - %s - %s" %( p.id,  p.apetrecho, p.nome, p.descricao ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblApetrechos.objects.order_by('id').all():
            result_id.append("%d" % p.id)
         return result_id
     

class TblMetodosManager(models.Manager):
    def sulta(self):
         result_list=[]
         
         for p in TblMetodos.objects.order_by('metodo').all():
             result_list.append("%d - %s - %s - %s - %s" %( p.id,  p.metodo, p.local,  p.nome, p.obs ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblMetodos.objects.order_by('metodo').all():
            result_id.append("%d" % p.id)
         return result_id
    

class TblAtrEtsManager(models.Manager):
    def sulta(self):
         result_list=[]
         
         for p in TblAtrEts.objects.order_by('medida').all():
             result_list.append("%d - %s - %s - %s" %( p.id,  p.medida, p.nome, p.descricao ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblAtrEts.objects.order_by('medida').all():
            result_id.append("%d" % p.id)
         return result_id
    

class TblInstrumentaisManager(models.Manager):
    def sulta(self):
         result_list=[]
         
         for p in TblInstrumentais.objects.order_by('apetrecho').all():
             result_list.append("%d - %s - %s - %100.2f -%s -%s" %( p.id,  p.apetrecho, p.atributo, p.valor,  p.unidade,  p.obs ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblInstrumentais.objects.order_by('apetrecho').all():
            result_id.append("%d" % p.id)
         return result_id

class TblMetInsManager(models.Manager):
    def sulta(self):
         result_list=[]
         
         for p in TblMetIns.objects.order_by('metodo').all():
             result_list.append("%d - %s - %s - %s" %( p.id,  p.metodo, p.apetrecho, p.quantidade) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblMetIns.objects.order_by('metodo').all():
            result_id.append("%d" % p.id)
         return result_id


class TblAtribs(models.Model):
    medida=models.CharField(u'Atributo',  max_length ='100',  unique=True)
    nome= models.CharField(u'Nome',  max_length='150',  unique=True)
    descricao= models.TextField(u'Descrição',  blank=True)
    objects=models.Manager()
#    atributo=TblAtributosManager()
    class Meta:
        db_table='tbl_atribs'
    def __unicode__(self):
        return unicode (self.medida)

        
class TblUnidades (models.Model):
    KINDS=(
        ('E',  (u'Espaço')), 
        ('T',  (u'Tempo')),
        ('O',  (u'Outros')),
    )
    KINDSS=(
        ('U',  (u'Unidimensional')), 
        ('B',  (u'Bidimensional')),
        ('T',  (u'Tridimensional')),
        
    )
    unidade= models.CharField (u'nome da unidade',  max_length='100', unique=True)
    nome=models.CharField (u'nome por extenso',  max_length='100',  blank=True)
    descricao= models.CharField (u'descrição',  max_length='250',  blank=True)
    esp_tem=models.CharField (u'espaço ou tempo',  max_length=1,  choices=KINDS,  blank=True)
    dimensao=models.CharField (u'dimensão', max_length=1, blank=True,  choices=KINDSS)
    
    objects=models.Manager()
    #unidad=TblUnidadesManager()
    class Meta:
        db_table='tbl_unidades'
        #ordering=["unidade"]
                    
    def __unicode__(self):
        return unicode (self.nome)

class TblLocais (models.Model):
    local=models.CharField(u'Local de amostragem',  max_length='200', blank=True,  null=True)
    descricao=models.TextField(u'descrição', blank=True,  null=True)
    objects=models.Manager()
    
    class Meta:
        db_table='tbl_locais'

    def __unicode__(self):
        return unicode (self.descricao)
        
class TblApetrechos (models.Model):
    apetrecho=models.CharField(u'apetrecho',  max_length='100',  unique=True)
    nome=models.CharField(u'nome por extenso',  max_length='150',  blank=True)
    descricao= models.CharField (u'descrição',  max_length='250',  blank=True)
    objects=models.Manager()
#    unidade=TblApetrechosManager()
    class Meta:
        db_table='tbl_apetrechos'
            
    def __unicode__(self):
        return unicode(self.apetrecho)
        
class TblMetodos(models.Model):
    metodo=models.CharField(u'Método',  max_length='100',  unique=True)
    local=models.ForeignKey(TblLocais)
    nome=models.CharField(u'nome por extenso',  max_length='100',  blank=True)
    obs=models.TextField(u'Observação',  blank=True)
    var_biodiv=models.TextField(blank=True)
    var_esforco=models.TextField(blank=True)
    objects=models.Manager()
#    metodo=TblMetodosManager()
    class Meta:
        db_table='tbl_metodos'
    
    def __unicode__(self):
        return unicode(self.metodo)

class TblAtrEts (models.Model):
    medida=models.CharField(u'Atributo',  max_length ='100',  unique=True)
    nome= models.CharField(u'Nome',  max_length='150',  blank=True)
    descricao= models.TextField(u'Descrição',  blank=True)
    objects=models.Manager()
   # medida_objects=TblAtrEts.objects.only('medida')   
    class Meta:
        db_table='tbl_atr_ets'
    def __unicode__(self):
        return unicode(self.medida)

class TblInstrumentais (models.Model):
    apetrecho=models.ForeignKey(TblApetrechos)
    atributo= models.ForeignKey(TblAtribs)
    unidade=models.ForeignKey(TblUnidades,  blank=True)
    valor=models.FloatField(u'Valor',  blank=True)
    obs= models.TextField(u'Observação',  blank=True)
    objects=models.Manager()
#    apetrecho=TbTblAtrEtslInstrumentaisManager()
    class Meta:
        db_table='tbl_instrumentais'

    def __unicode__(self):
        return unicode([self.apetrecho,  self.atributo,  self.unidade,  self.valor])    

class TblMetIns (models.Model):
    metodo=models.ForeignKey(TblMetodos)
    apetrecho=models.ForeignKey(TblApetrechos)
    quantidade=models.IntegerField(u'quantidade por estacao',  null=True)
    objects=models.Manager()
 #   metodo=TblMetInsManager()

    class Meta:
        db_table='tbl_metins'
    
    def __unicode__(self):
        return unicode(self.metodo)

class TblMetAtEtsManager(models.Manager):
    def sulta(self):
         result_list=[]
         
         for p in TblMetAtEts.objects.order_by('metodo').all():
             result_list.append("%d - %s - %s - %s -%s -%s -%s" %( p.id,  p.metodo, p.atributo_estacao, p.atributo, p.valor, p.unidade,   p.obs) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblMetAtEts.objects.order_by('metodo').all():
            result_id.append("%d" % p.id)
         return result_id

'''  c=TblMetAtEts.objects.all()
        la=[p.metodo for p in c]
        lb=[p.atributo_estacao for p in c]
        lc=[p.atributo for p in c]
        ld=[p.valor for p in c]
        le=[p.unidade for p in c]
        lf=[p.obs for p in c]
        result_list=[]
        for e, i in enumerate (la):
            for ee, ii in enumerate (lb):
                for eee, iii in enumerate (lc):
                    for eeee, iiii in enumerate (ld):
                        for eeeee, iiiii in enumerate (le):
                            for eeeeee, iiiiii in enumerate (lf):
                                if e==ee==eee==eeee==eeeee==eeeeee:
                                    result_list.append("%s - %s - %s - %s - %s - %s" %(i, ii, iii, iiii,  iiiii,  iiiiii))
        return result_list'''
class TblMetAtEts(models.Model):
    metodo=models.ForeignKey(TblMetodos)
    
    atributo_estacao=models.ForeignKey(TblAtrEts,  blank=True,  help_text='coloque o metodo')
    atributo= models.ForeignKey(TblAtribs,  blank=True,  null=True)
    unidade=models.ForeignKey(TblUnidades,  blank=True,  null=True)
    valor=models.FloatField(u'Valor',  blank=True,  null=True)
    obs= models.TextField(u'Observação',  blank=True)
    objects=models.Manager()
#    metodo=TblMetAtEtsManager()

    class Meta:
        db_table='tbl_metatets'

    def __unicode__(self):
        return unicode(self.metodo)
