#-*- coding: utf-8 -*-

from grempres.models import TblEmpreendimentos,  TblPessoas
#import gratributos
#from gratributos import models
from gratributos.models import TblAtributos
from django.db import models
from grmetodos.models import TblMetodos
import grempres
#from grempres.models import *

class TblCampanhas(models.Model):
    
    empreendimento = models.ForeignKey(TblEmpreendimentos)
    pessoa = models.ForeignKey(TblPessoas,   blank=True)
    descricao = models.CharField(max_length=200,  blank=True)
    dt_inicio = models.DateField()
    dt_fim = models.DateField(blank=True)
    precip_periodo = models.FloatField(blank=True)
    temp_periodo = models.FloatField(blank=True)
    metodo = models.ForeignKey(TblMetodos)
    pessoa2 = models.IntegerField(blank=True)
    num_campanha = models.IntegerField()
    class Meta:
        db_table = u'tbl_campanhas'

class TblLevantamentos(models.Model):
   
    metodo = models.ForeignKey(TblMetodos)
    empreendimento = models.IntegerField()
    campanha = models.ForeignKey(TblCampanhas,  blank=True)
    descricao = models.CharField(max_length=20,  blank=True)
    dt_inicial = models.DateField()
    dt_final = models.DateField(blank=True)
    hr_inicial = models.TimeField( blank=True)
    hr_final = models.TimeField(blank=True)
    temp_inicial = models.FloatField(blank=True)
    temp_final = models.FloatField(blank=True)
    tipo_ua = models.CharField(max_length=1,  blank=True)
    id_ua = models.IntegerField(blank=True)
    class Meta:
        db_table = u'tbl_levantamentos'

class TblCoordenadas(models.Model):
    
    orientacao = models.CharField(max_length=8)
    datum = models.CharField(max_length=25)
    nome = models.CharField(max_length=45)
    localidade = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        db_table = u'tbl_coordenadas'
        
class TblAbioDados(models.Model):
  
    levantamento = models.ForeignKey(TblLevantamentos)
    coordenada = models.ForeignKey(TblCoordenadas)
    class Meta:
        db_table = u'tbl_abio_dados'

class TblAbioticosDate(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    dados_abioticos = models.ForeignKey(TblAbioDados)
    valor = models.DateField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_abioticos_date'

class TblAbioticosFloat(models.Model):
    iatributo = models.ForeignKey(TblAtributos)
    idados_abioticos = models.ForeignKey(TblAbioDados)
    valor = models.FloatField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_abioticos_float'

class TblAbioticosInteger(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    dados_abioticos = models.ForeignKey(TblAbioDados)
    valor = models.IntegerField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_abioticos_integer'

class TblAbioticosText(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    dados_abioticos = models.ForeignKey(TblAbioDados)
    valor = models.TextField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_abioticos_text'

class TblAbioticosTime(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    dados_abioticos = models.ForeignKey(TblAbioDados)
    valor = models.TimeField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_abioticos_time'

class TblAbioticosVarchar(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    dados_abioticos = models.ForeignKey(TblAbioDados)
    valor = models.CharField(max_length=255)
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_abioticos_varchar'


class TblDadosColetaAvulsa(models.Model):
    col_avulsa = models.IntegerField(primary_key=True)
    coordenada = models.ForeignKey(TblCoordenadas)
    empreendimento = models.IntegerField()
    campanha = models.ForeignKey(TblCampanhas)
    class Meta:
        db_table = u'tbl_dados_coleta_avulsa'

class TblAnimaisDados(models.Model):
    
    col_avulsa = models.ForeignKey(TblDadosColetaAvulsa,  blank=True)
    levantamento = models.ForeignKey(TblLevantamentos)
    filo = models.CharField(max_length=45,  blank=True)
    classe = models.CharField(max_length=45,  blank=True)
    ordem = models.CharField(max_length=45,  blank=True)
    familia = models.CharField(max_length=45,  blank=True)
    genero = models.CharField(max_length=45,  blank=True)
    imprecisao_determinacao = models.CharField(max_length=45,  blank=True)
    epiteto_especifico = models.CharField(max_length=45,  blank=True)
    autor_epiteto_especifico = models.CharField(max_length=100,  blank=True)
    ano_autor_epiteto_especifico = models.CharField(max_length=20,  blank=True)
    coletor = models.CharField(max_length=45,  blank=True)
    numero_coleta = models.CharField(max_length=20,  blank=True)
    lote_individuo = models.CharField(max_length=20,  blank=True)
    coleta_avulsa = models.BooleanField()
    posicionamento = models.CharField(max_length=1,  blank=True)
    superfamilia = models.CharField(max_length=65,  blank=True)
    subfamilia = models.CharField(max_length=65,  blank=True)
    tribo = models.CharField(max_length=65,  blank=True)
    subtribo = models.CharField(max_length=65,  blank=True)
    class Meta:
        db_table = u'tbl_animais_dados'

class TblAnimaisDate(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_animal = models.ForeignKey(TblAnimaisDados)
    valor = models.DateField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_animais_date'

class TblAnimaisFloat(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_animal = models.ForeignKey(TblAnimaisDados)
    valor = models.FloatField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_animais_float'

class TblAnimaisInteger(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_animal = models.ForeignKey(TblAnimaisDados)
    valor = models.IntegerField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_animais_integer'

class TblAnimaisText(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_animal = models.ForeignKey(TblAnimaisDados)
    valor = models.TextField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_animais_text'

class TblAnimaisTime(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_animal = models.ForeignKey(TblAnimaisDados)
    valor = models.TimeField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_animais_time'

class TblAnimaisVarchar(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_animal = models.ForeignKey(TblAnimaisDados)
    valor = models.CharField(max_length=255)
    situacao = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'tbl_animais_varchar'

class TblGradesModulos(models.Model):
    empreendimento = models.ForeignKey(TblEmpreendimentos)    
    pessoa = models.ForeignKey(TblPessoas)    
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1)
    qnt_trilhas = models.IntegerField()
    abrev = models.CharField(max_length=20)
    class Meta:
        db_table = u'tbl_grades_modulos'
        
class TblTrilhas(models.Model):
   
    grade_modulo = models.ForeignKey(TblGradesModulos)
    nome = models.CharField(max_length=20)
    comp = models.IntegerField(blank=True)
    tipo_ua = models.CharField(max_length=1)
    class Meta:
        db_table = u'tbl_trilhas'

class TblParcelas(models.Model):
  
    trilha = models.ForeignKey(TblTrilhas)
    nome = models.CharField(max_length=80)
    dist_paralela_trilha = models.IntegerField(blank=True)
    dist_perpend_trilha = models.IntegerField(blank=True)
    tipo_ua = models.CharField(max_length=1)
    segue_curva_nivel = models.BooleanField()
    comprimento = models.FloatField(blank=True)
    obs = models.TextField(blank=True)
    class Meta:
        db_table = u'tbl_parcelas'
        
class TblParcelasCoord(models.Model):
  
    coordenada = models.ForeignKey(TblCoordenadas)
    parcela = models.ForeignKey(TblParcelas)
    num_piquete = models.IntegerField(blank=True)
    class Meta:
        db_table = u'tbl_parcelas_coord'

class TblPlantasDados(models.Model):
   
    col_avulsa = models.ForeignKey(TblDadosColetaAvulsa)
    levantamento = models.ForeignKey(TblLevantamentos)
    divisao = models.CharField(max_length=45,  blank=True)
    classe = models.CharField(max_length=45,  blank=True)
    ordem = models.CharField(max_length=45,  blank=True)
    familia = models.CharField(max_length=45,  blank=True)
    genero = models.CharField(max_length=45,  blank=True)
    imprecisao_determinacao = models.CharField(max_length=10,  blank=True)
    epiteto_especifico = models.CharField(max_length=45,  blank=True)
    autor_epiteto_especifico = models.CharField(max_length=100,  blank=True)
    variedade = models.CharField(max_length=255,  blank=True)
    autor_variedade = models.CharField(max_length=100,  blank=True)
    coletor = models.CharField(max_length=45,  blank=True)
    numero_coleta = models.CharField(max_length=20,  blank=True)
    coleta_avulsa = models.BooleanField()
    posicionamento = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_plantas_dados'

class TblPlantasDate(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_plantas = models.ForeignKey(TblPlantasDados)
    valor = models.DateField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_plantas_date'

class TblPlantasFloat(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_plantas = models.ForeignKey(TblPlantasDados)
    valor = models.FloatField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_plantas_float'

class TblPlantasInteger(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_plantas = models.ForeignKey(TblPlantasDados)
    valor = models.IntegerField()
    situacao = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'tbl_plantas_integer'

class TblPlantasText(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_plantas = models.ForeignKey(TblPlantasDados)
    valor = models.TextField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_plantas_text'

class TblPlantasTime(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_plantas = models.ForeignKey(TblPlantasDados)
    valor = models.TimeField()
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_plantas_time'

class TblPlantasVarchar(models.Model):
    atributo = models.ForeignKey(TblAtributos)
    tbl_plantas = models.ForeignKey(TblPlantasDados)
    valor = models.CharField(max_length=255)
    situacao = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_plantas_varchar'

class TblSegmentos(models.Model):
    
    coordenada = models.ForeignKey(TblCoordenadas)
    parcela = models.ForeignKey(TblParcelas)
    nome = models.CharField(max_length=15,  blank=True)
    posicao = models.IntegerField(blank=True)
    num_piquete_inicial = models.IntegerField(blank=True)
    continuo = models.BooleanField(blank=True)
    class Meta:
        db_table = u'tbl_segmentos'


class TblTrilhasCoord(models.Model):
   
    coordenada = models.ForeignKey(TblCoordenadas)
    trilha = models.ForeignKey(TblTrilhas)
    num_piquete = models.IntegerField(blank=True)
    class Meta:
        db_table = u'tbl_trilhas_coord'

class TblUaAvulsas(models.Model):
  
    descricao = models.TextField(blank=True)
    comprimento = models.FloatField(blank=True)
    segue_curva_nivel = models.BooleanField(blank=True)
    class Meta:
        db_table = u'tbl_ua_avulsas'


class TblUaAvulsasCoord(models.Model):
    
    coordenada = models.ForeignKey(TblCoordenadas)
    ua_avulsa = models.ForeignKey(TblUaAvulsas)
    ponto_referencia = models.CharField(max_length=1,  blank=True)
    class Meta:
        db_table = u'tbl_ua_avulsas_coord'
