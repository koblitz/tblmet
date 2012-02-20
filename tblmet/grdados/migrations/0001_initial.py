# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TblCampanhas'
        db.create_table(u'tbl_campanhas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empreendimento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grempres.TblEmpreendimentos'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grempres.TblPessoas'], blank=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dt_inicio', self.gf('django.db.models.fields.DateField')()),
            ('dt_fim', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('precip_periodo', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('temp_periodo', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('metodo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblMetodos'])),
            ('pessoa2', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('num_campanha', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('grdados', ['TblCampanhas'])

        # Adding model 'TblLevantamentos'
        db.create_table(u'tbl_levantamentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metodo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblMetodos'])),
            ('empreendimento', self.gf('django.db.models.fields.IntegerField')()),
            ('campanha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCampanhas'], blank=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('dt_inicial', self.gf('django.db.models.fields.DateField')()),
            ('dt_final', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('hr_inicial', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('hr_final', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('temp_inicial', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('temp_final', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('tipo_ua', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('id_ua', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('grdados', ['TblLevantamentos'])

        # Adding model 'TblCoordenadas'
        db.create_table(u'tbl_coordenadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orientacao', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('datum', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('localidade', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('grdados', ['TblCoordenadas'])

        # Adding model 'TblAbioDados'
        db.create_table(u'tbl_abio_dados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('levantamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblLevantamentos'])),
            ('coordenada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCoordenadas'])),
        ))
        db.send_create_signal('grdados', ['TblAbioDados'])

        # Adding model 'TblAbioticosDate'
        db.create_table(u'tbl_abioticos_date', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('dados_abioticos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAbioDados'])),
            ('valor', self.gf('django.db.models.fields.DateField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAbioticosDate'])

        # Adding model 'TblAbioticosFloat'
        db.create_table(u'tbl_abioticos_float', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iatributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('idados_abioticos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAbioDados'])),
            ('valor', self.gf('django.db.models.fields.FloatField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAbioticosFloat'])

        # Adding model 'TblAbioticosInteger'
        db.create_table(u'tbl_abioticos_integer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('dados_abioticos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAbioDados'])),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAbioticosInteger'])

        # Adding model 'TblAbioticosText'
        db.create_table(u'tbl_abioticos_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('dados_abioticos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAbioDados'])),
            ('valor', self.gf('django.db.models.fields.TextField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAbioticosText'])

        # Adding model 'TblAbioticosTime'
        db.create_table(u'tbl_abioticos_time', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('dados_abioticos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAbioDados'])),
            ('valor', self.gf('django.db.models.fields.TimeField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAbioticosTime'])

        # Adding model 'TblAbioticosVarchar'
        db.create_table(u'tbl_abioticos_varchar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('dados_abioticos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAbioDados'])),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAbioticosVarchar'])

        # Adding model 'TblDadosColetaAvulsa'
        db.create_table(u'tbl_dados_coleta_avulsa', (
            ('col_avulsa', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('coordenada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCoordenadas'])),
            ('empreendimento', self.gf('django.db.models.fields.IntegerField')()),
            ('campanha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCampanhas'])),
        ))
        db.send_create_signal('grdados', ['TblDadosColetaAvulsa'])

        # Adding model 'TblAnimaisDados'
        db.create_table(u'tbl_animais_dados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('col_avulsa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblDadosColetaAvulsa'], blank=True)),
            ('levantamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblLevantamentos'])),
            ('filo', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('classe', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('ordem', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('familia', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('imprecisao_determinacao', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('epiteto_especifico', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('autor_epiteto_especifico', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('ano_autor_epiteto_especifico', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('coletor', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('numero_coleta', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('lote_individuo', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('coleta_avulsa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posicionamento', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('superfamilia', self.gf('django.db.models.fields.CharField')(max_length=65, blank=True)),
            ('subfamilia', self.gf('django.db.models.fields.CharField')(max_length=65, blank=True)),
            ('tribo', self.gf('django.db.models.fields.CharField')(max_length=65, blank=True)),
            ('subtribo', self.gf('django.db.models.fields.CharField')(max_length=65, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAnimaisDados'])

        # Adding model 'TblAnimaisDate'
        db.create_table(u'tbl_animais_date', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAnimaisDados'])),
            ('valor', self.gf('django.db.models.fields.DateField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAnimaisDate'])

        # Adding model 'TblAnimaisFloat'
        db.create_table(u'tbl_animais_float', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAnimaisDados'])),
            ('valor', self.gf('django.db.models.fields.FloatField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAnimaisFloat'])

        # Adding model 'TblAnimaisInteger'
        db.create_table(u'tbl_animais_integer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAnimaisDados'])),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAnimaisInteger'])

        # Adding model 'TblAnimaisText'
        db.create_table(u'tbl_animais_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAnimaisDados'])),
            ('valor', self.gf('django.db.models.fields.TextField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAnimaisText'])

        # Adding model 'TblAnimaisTime'
        db.create_table(u'tbl_animais_time', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAnimaisDados'])),
            ('valor', self.gf('django.db.models.fields.TimeField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAnimaisTime'])

        # Adding model 'TblAnimaisVarchar'
        db.create_table(u'tbl_animais_varchar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblAnimaisDados'])),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('situacao', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grdados', ['TblAnimaisVarchar'])

        # Adding model 'TblGradesModulos'
        db.create_table(u'tbl_grades_modulos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empreendimento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grempres.TblEmpreendimentos'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grempres.TblPessoas'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('qnt_trilhas', self.gf('django.db.models.fields.IntegerField')()),
            ('abrev', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('grdados', ['TblGradesModulos'])

        # Adding model 'TblTrilhas'
        db.create_table(u'tbl_trilhas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade_modulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblGradesModulos'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('comp', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('tipo_ua', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('grdados', ['TblTrilhas'])

        # Adding model 'TblParcelas'
        db.create_table(u'tbl_parcelas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trilha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblTrilhas'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('dist_paralela_trilha', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('dist_perpend_trilha', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('tipo_ua', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('segue_curva_nivel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comprimento', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grdados', ['TblParcelas'])

        # Adding model 'TblParcelasCoord'
        db.create_table(u'tbl_parcelas_coord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coordenada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCoordenadas'])),
            ('parcela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblParcelas'])),
            ('num_piquete', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('grdados', ['TblParcelasCoord'])

        # Adding model 'TblPlantasDados'
        db.create_table(u'tbl_plantas_dados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('col_avulsa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblDadosColetaAvulsa'])),
            ('levantamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblLevantamentos'])),
            ('divisao', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('classe', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('ordem', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('familia', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('imprecisao_determinacao', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('epiteto_especifico', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('autor_epiteto_especifico', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('variedade', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('autor_variedade', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('coletor', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('numero_coleta', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('coleta_avulsa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posicionamento', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblPlantasDados'])

        # Adding model 'TblPlantasDate'
        db.create_table(u'tbl_plantas_date', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_plantas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblPlantasDados'])),
            ('valor', self.gf('django.db.models.fields.DateField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblPlantasDate'])

        # Adding model 'TblPlantasFloat'
        db.create_table(u'tbl_plantas_float', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_plantas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblPlantasDados'])),
            ('valor', self.gf('django.db.models.fields.FloatField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblPlantasFloat'])

        # Adding model 'TblPlantasInteger'
        db.create_table(u'tbl_plantas_integer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_plantas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblPlantasDados'])),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblPlantasInteger'])

        # Adding model 'TblPlantasText'
        db.create_table(u'tbl_plantas_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_plantas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblPlantasDados'])),
            ('valor', self.gf('django.db.models.fields.TextField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblPlantasText'])

        # Adding model 'TblPlantasTime'
        db.create_table(u'tbl_plantas_time', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_plantas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblPlantasDados'])),
            ('valor', self.gf('django.db.models.fields.TimeField')()),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblPlantasTime'])

        # Adding model 'TblPlantasVarchar'
        db.create_table(u'tbl_plantas_varchar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gratributos.TblAtributos'])),
            ('tbl_plantas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblPlantasDados'])),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblPlantasVarchar'])

        # Adding model 'TblSegmentos'
        db.create_table(u'tbl_segmentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coordenada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCoordenadas'])),
            ('parcela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblParcelas'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('posicao', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('num_piquete_inicial', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('continuo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('grdados', ['TblSegmentos'])

        # Adding model 'TblTrilhasCoord'
        db.create_table(u'tbl_trilhas_coord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coordenada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCoordenadas'])),
            ('trilha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblTrilhas'])),
            ('num_piquete', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('grdados', ['TblTrilhasCoord'])

        # Adding model 'TblUaAvulsas'
        db.create_table(u'tbl_ua_avulsas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comprimento', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('segue_curva_nivel', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('grdados', ['TblUaAvulsas'])

        # Adding model 'TblUaAvulsasCoord'
        db.create_table(u'tbl_ua_avulsas_coord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coordenada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblCoordenadas'])),
            ('ua_avulsa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grdados.TblUaAvulsas'])),
            ('ponto_referencia', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grdados', ['TblUaAvulsasCoord'])


    def backwards(self, orm):
        
        # Deleting model 'TblCampanhas'
        db.delete_table(u'tbl_campanhas')

        # Deleting model 'TblLevantamentos'
        db.delete_table(u'tbl_levantamentos')

        # Deleting model 'TblCoordenadas'
        db.delete_table(u'tbl_coordenadas')

        # Deleting model 'TblAbioDados'
        db.delete_table(u'tbl_abio_dados')

        # Deleting model 'TblAbioticosDate'
        db.delete_table(u'tbl_abioticos_date')

        # Deleting model 'TblAbioticosFloat'
        db.delete_table(u'tbl_abioticos_float')

        # Deleting model 'TblAbioticosInteger'
        db.delete_table(u'tbl_abioticos_integer')

        # Deleting model 'TblAbioticosText'
        db.delete_table(u'tbl_abioticos_text')

        # Deleting model 'TblAbioticosTime'
        db.delete_table(u'tbl_abioticos_time')

        # Deleting model 'TblAbioticosVarchar'
        db.delete_table(u'tbl_abioticos_varchar')

        # Deleting model 'TblDadosColetaAvulsa'
        db.delete_table(u'tbl_dados_coleta_avulsa')

        # Deleting model 'TblAnimaisDados'
        db.delete_table(u'tbl_animais_dados')

        # Deleting model 'TblAnimaisDate'
        db.delete_table(u'tbl_animais_date')

        # Deleting model 'TblAnimaisFloat'
        db.delete_table(u'tbl_animais_float')

        # Deleting model 'TblAnimaisInteger'
        db.delete_table(u'tbl_animais_integer')

        # Deleting model 'TblAnimaisText'
        db.delete_table(u'tbl_animais_text')

        # Deleting model 'TblAnimaisTime'
        db.delete_table(u'tbl_animais_time')

        # Deleting model 'TblAnimaisVarchar'
        db.delete_table(u'tbl_animais_varchar')

        # Deleting model 'TblGradesModulos'
        db.delete_table(u'tbl_grades_modulos')

        # Deleting model 'TblTrilhas'
        db.delete_table(u'tbl_trilhas')

        # Deleting model 'TblParcelas'
        db.delete_table(u'tbl_parcelas')

        # Deleting model 'TblParcelasCoord'
        db.delete_table(u'tbl_parcelas_coord')

        # Deleting model 'TblPlantasDados'
        db.delete_table(u'tbl_plantas_dados')

        # Deleting model 'TblPlantasDate'
        db.delete_table(u'tbl_plantas_date')

        # Deleting model 'TblPlantasFloat'
        db.delete_table(u'tbl_plantas_float')

        # Deleting model 'TblPlantasInteger'
        db.delete_table(u'tbl_plantas_integer')

        # Deleting model 'TblPlantasText'
        db.delete_table(u'tbl_plantas_text')

        # Deleting model 'TblPlantasTime'
        db.delete_table(u'tbl_plantas_time')

        # Deleting model 'TblPlantasVarchar'
        db.delete_table(u'tbl_plantas_varchar')

        # Deleting model 'TblSegmentos'
        db.delete_table(u'tbl_segmentos')

        # Deleting model 'TblTrilhasCoord'
        db.delete_table(u'tbl_trilhas_coord')

        # Deleting model 'TblUaAvulsas'
        db.delete_table(u'tbl_ua_avulsas')

        # Deleting model 'TblUaAvulsasCoord'
        db.delete_table(u'tbl_ua_avulsas_coord')


    models = {
        'gratributos.tblatributos': {
            'Meta': {'object_name': 'TblAtributos', 'db_table': "'tbl_atributos'"},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'no_at_ca_co': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': "'1'"}),
            'tipo_valor': ('django.db.models.fields.CharField', [], {'max_length': "'1'"}),
            'unidade_utilizada': ('django.db.models.fields.CharField', [], {'max_length': "'60'"})
        },
        'grdados.tblabiodados': {
            'Meta': {'object_name': 'TblAbioDados', 'db_table': "u'tbl_abio_dados'"},
            'coordenada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCoordenadas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levantamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblLevantamentos']"})
        },
        'grdados.tblabioticosdate': {
            'Meta': {'object_name': 'TblAbioticosDate', 'db_table': "u'tbl_abioticos_date'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'dados_abioticos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAbioDados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'valor': ('django.db.models.fields.DateField', [], {})
        },
        'grdados.tblabioticosfloat': {
            'Meta': {'object_name': 'TblAbioticosFloat', 'db_table': "u'tbl_abioticos_float'"},
            'iatributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idados_abioticos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAbioDados']"}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {})
        },
        'grdados.tblabioticosinteger': {
            'Meta': {'object_name': 'TblAbioticosInteger', 'db_table': "u'tbl_abioticos_integer'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'dados_abioticos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAbioDados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        'grdados.tblabioticostext': {
            'Meta': {'object_name': 'TblAbioticosText', 'db_table': "u'tbl_abioticos_text'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'dados_abioticos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAbioDados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'valor': ('django.db.models.fields.TextField', [], {})
        },
        'grdados.tblabioticostime': {
            'Meta': {'object_name': 'TblAbioticosTime', 'db_table': "u'tbl_abioticos_time'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'dados_abioticos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAbioDados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'valor': ('django.db.models.fields.TimeField', [], {})
        },
        'grdados.tblabioticosvarchar': {
            'Meta': {'object_name': 'TblAbioticosVarchar', 'db_table': "u'tbl_abioticos_varchar'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'dados_abioticos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAbioDados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'grdados.tblanimaisdados': {
            'Meta': {'object_name': 'TblAnimaisDados', 'db_table': "u'tbl_animais_dados'"},
            'ano_autor_epiteto_especifico': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'autor_epiteto_especifico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'classe': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'col_avulsa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblDadosColetaAvulsa']", 'blank': 'True'}),
            'coleta_avulsa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coletor': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'epiteto_especifico': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'familia': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'filo': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imprecisao_determinacao': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'levantamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblLevantamentos']"}),
            'lote_individuo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'numero_coleta': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'posicionamento': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'subfamilia': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'subtribo': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'superfamilia': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'tribo': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'})
        },
        'grdados.tblanimaisdate': {
            'Meta': {'object_name': 'TblAnimaisDate', 'db_table': "u'tbl_animais_date'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAnimaisDados']"}),
            'valor': ('django.db.models.fields.DateField', [], {})
        },
        'grdados.tblanimaisfloat': {
            'Meta': {'object_name': 'TblAnimaisFloat', 'db_table': "u'tbl_animais_float'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAnimaisDados']"}),
            'valor': ('django.db.models.fields.FloatField', [], {})
        },
        'grdados.tblanimaisinteger': {
            'Meta': {'object_name': 'TblAnimaisInteger', 'db_table': "u'tbl_animais_integer'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAnimaisDados']"}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        'grdados.tblanimaistext': {
            'Meta': {'object_name': 'TblAnimaisText', 'db_table': "u'tbl_animais_text'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAnimaisDados']"}),
            'valor': ('django.db.models.fields.TextField', [], {})
        },
        'grdados.tblanimaistime': {
            'Meta': {'object_name': 'TblAnimaisTime', 'db_table': "u'tbl_animais_time'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAnimaisDados']"}),
            'valor': ('django.db.models.fields.TimeField', [], {})
        },
        'grdados.tblanimaisvarchar': {
            'Meta': {'object_name': 'TblAnimaisVarchar', 'db_table': "u'tbl_animais_varchar'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tbl_animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblAnimaisDados']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'grdados.tblcampanhas': {
            'Meta': {'object_name': 'TblCampanhas', 'db_table': "u'tbl_campanhas'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dt_fim': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'dt_inicio': ('django.db.models.fields.DateField', [], {}),
            'empreendimento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grempres.TblEmpreendimentos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblMetodos']"}),
            'num_campanha': ('django.db.models.fields.IntegerField', [], {}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grempres.TblPessoas']", 'blank': 'True'}),
            'pessoa2': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'precip_periodo': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'temp_periodo': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'grdados.tblcoordenadas': {
            'Meta': {'object_name': 'TblCoordenadas', 'db_table': "u'tbl_coordenadas'"},
            'datum': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'localidade': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'orientacao': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'grdados.tbldadoscoletaavulsa': {
            'Meta': {'object_name': 'TblDadosColetaAvulsa', 'db_table': "u'tbl_dados_coleta_avulsa'"},
            'campanha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCampanhas']"}),
            'col_avulsa': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'coordenada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCoordenadas']"}),
            'empreendimento': ('django.db.models.fields.IntegerField', [], {})
        },
        'grdados.tblgradesmodulos': {
            'Meta': {'object_name': 'TblGradesModulos', 'db_table': "u'tbl_grades_modulos'"},
            'abrev': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'empreendimento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grempres.TblEmpreendimentos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grempres.TblPessoas']"}),
            'qnt_trilhas': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'grdados.tbllevantamentos': {
            'Meta': {'object_name': 'TblLevantamentos', 'db_table': "u'tbl_levantamentos'"},
            'campanha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCampanhas']", 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'dt_final': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'dt_inicial': ('django.db.models.fields.DateField', [], {}),
            'empreendimento': ('django.db.models.fields.IntegerField', [], {}),
            'hr_final': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'hr_inicial': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_ua': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'metodo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblMetodos']"}),
            'temp_final': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'temp_inicial': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'tipo_ua': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'grdados.tblparcelas': {
            'Meta': {'object_name': 'TblParcelas', 'db_table': "u'tbl_parcelas'"},
            'comprimento': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'dist_paralela_trilha': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'dist_perpend_trilha': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'segue_curva_nivel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_ua': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'trilha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblTrilhas']"})
        },
        'grdados.tblparcelascoord': {
            'Meta': {'object_name': 'TblParcelasCoord', 'db_table': "u'tbl_parcelas_coord'"},
            'coordenada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCoordenadas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_piquete': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'parcela': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblParcelas']"})
        },
        'grdados.tblplantasdados': {
            'Meta': {'object_name': 'TblPlantasDados', 'db_table': "u'tbl_plantas_dados'"},
            'autor_epiteto_especifico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'autor_variedade': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'classe': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'col_avulsa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblDadosColetaAvulsa']"}),
            'coleta_avulsa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coletor': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'divisao': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'epiteto_especifico': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'familia': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imprecisao_determinacao': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'levantamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblLevantamentos']"}),
            'numero_coleta': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'posicionamento': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'variedade': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'grdados.tblplantasdate': {
            'Meta': {'object_name': 'TblPlantasDate', 'db_table': "u'tbl_plantas_date'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_plantas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblPlantasDados']"}),
            'valor': ('django.db.models.fields.DateField', [], {})
        },
        'grdados.tblplantasfloat': {
            'Meta': {'object_name': 'TblPlantasFloat', 'db_table': "u'tbl_plantas_float'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_plantas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblPlantasDados']"}),
            'valor': ('django.db.models.fields.FloatField', [], {})
        },
        'grdados.tblplantasinteger': {
            'Meta': {'object_name': 'TblPlantasInteger', 'db_table': "u'tbl_plantas_integer'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_plantas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblPlantasDados']"}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        'grdados.tblplantastext': {
            'Meta': {'object_name': 'TblPlantasText', 'db_table': "u'tbl_plantas_text'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_plantas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblPlantasDados']"}),
            'valor': ('django.db.models.fields.TextField', [], {})
        },
        'grdados.tblplantastime': {
            'Meta': {'object_name': 'TblPlantasTime', 'db_table': "u'tbl_plantas_time'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_plantas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblPlantasDados']"}),
            'valor': ('django.db.models.fields.TimeField', [], {})
        },
        'grdados.tblplantasvarchar': {
            'Meta': {'object_name': 'TblPlantasVarchar', 'db_table': "u'tbl_plantas_varchar'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gratributos.TblAtributos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tbl_plantas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblPlantasDados']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'grdados.tblsegmentos': {
            'Meta': {'object_name': 'TblSegmentos', 'db_table': "u'tbl_segmentos'"},
            'continuo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coordenada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCoordenadas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'num_piquete_inicial': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'parcela': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblParcelas']"}),
            'posicao': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        'grdados.tbltrilhas': {
            'Meta': {'object_name': 'TblTrilhas', 'db_table': "u'tbl_trilhas'"},
            'comp': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'grade_modulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblGradesModulos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tipo_ua': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'grdados.tbltrilhascoord': {
            'Meta': {'object_name': 'TblTrilhasCoord', 'db_table': "u'tbl_trilhas_coord'"},
            'coordenada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCoordenadas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_piquete': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'trilha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblTrilhas']"})
        },
        'grdados.tbluaavulsas': {
            'Meta': {'object_name': 'TblUaAvulsas', 'db_table': "u'tbl_ua_avulsas'"},
            'comprimento': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segue_curva_nivel': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'grdados.tbluaavulsascoord': {
            'Meta': {'object_name': 'TblUaAvulsasCoord', 'db_table': "u'tbl_ua_avulsas_coord'"},
            'coordenada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblCoordenadas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ponto_referencia': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ua_avulsa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grdados.TblUaAvulsas']"})
        },
        'grempres.tblempreendimentos': {
            'Meta': {'object_name': 'TblEmpreendimentos', 'db_table': "u'tbl_empreendimentos'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'num_processo': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'grempres.tblempresas': {
            'Meta': {'object_name': 'TblEmpresas', 'db_table': "u'tbl_empresas'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'empreendimento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grempres.TblEmpreendimentos']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'grempres.tblpessoas': {
            'Meta': {'object_name': 'TblPessoas', 'db_table': "u'tbl_pessoas'"},
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'CPF'", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grempres.TblEmpresas']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_lattes': ('django.db.models.fields.URLField', [], {'max_length': '80', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telefone_princ': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'telefone_sec': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'grmetodos.tbllocais': {
            'Meta': {'object_name': 'TblLocais', 'db_table': "'tbl_locais'"},
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'})
        },
        'grmetodos.tblmetodos': {
            'Meta': {'object_name': 'TblMetodos', 'db_table': "'tbl_metodos'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblLocais']"}),
            'metodo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'100'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'var_biodiv': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'var_esforco': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['grdados']
