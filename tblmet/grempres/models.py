
from django.db import models
class TblEmpreendimentosManager(models.Manager):
  
    def sulta(self):
         result_list=[]
         
         for p in TblEmpreendimentos.objects.order_by('id').all():
             
             result_list.append("%d - %s - %s - %s" %( p.id,  p.nome, p.num_processo, p.descricao ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblEmpreendimentos.objects.all():
            result_id.append("%d" % p.id)
         return result_id
class TblEmpreendimentos(models.Model):
    nome = models.CharField(max_length=80)
    num_processo = models.CharField(max_length=25)
    descricao = models.CharField(max_length=350,   blank=True)
    obs=models.TextField(blank=True)
    objects=models.Manager()
    class Meta:
        db_table = u'tbl_empreendimentos'
    def __unicode__(self):
        return unicode (self.nome)        
class TblEmpresasManager(models.Manager):
  
    def sulta(self):
         result_list=[]
         
         for p in TblEmpresas.objects.order_by('id').all():
             
             result_list.append("%d - %s - %s" %( p.id,  p.nome, p.descricao ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblEmpresas.objects.all():
            result_id.append("%d" % p.id)
         return result_id
class TblEmpresas(models.Model):
    empreendimento = models.ForeignKey(TblEmpreendimentos, blank=True)
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=300,   blank=True)
    objects=models.Manager()
    class Meta:
        db_table = u'tbl_empresas'
    def __unicode__(self):
        return unicode (self.nome)        

class TblPessoasManager(models.Manager):
  
    def sulta(self):
         result_list=[]
         
         for p in TblPessoas.objects.order_by('id').all():
             
             result_list.append("%d - %s - %s - %s" %( p.id,  p.nome, p.email, p.obs ) )
            
         return result_list
    def sultaid(self):
         result_id=[] 
         for p in TblPessoas.objects.all():
            result_id.append("%d" % p.id)
         return result_id

class TblPessoas(models.Model):
    empresa = models.ForeignKey(TblEmpresas,   blank=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50, db_column='CPF',   blank=True) # Field name made lowercase.
    link_lattes = models.URLField(max_length=80,  blank=True)
    email = models.EmailField(max_length=50,   blank=True)
    telefone_princ = models.CharField(max_length=15,   blank=True)
    telefone_sec = models.CharField(max_length=15,   blank=True)
    obs=models.TextField(blank=True)
    objects=models.Manager()
    class Meta:
        db_table = u'tbl_pessoas'
    def __unicode__(self):
        return unicode (self.nome)        
