# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TblAtribs'
        db.create_table('tbl_atribs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medida', self.gf('django.db.models.fields.CharField')(unique=True, max_length='100')),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length='150')),
            ('descricao', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblAtribs'])

        # Adding model 'TblUnidades'
        db.create_table('tbl_unidades', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unidade', self.gf('django.db.models.fields.CharField')(unique=True, max_length='100')),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length='250', blank=True)),
            ('esp_tem', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('dimensao', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblUnidades'])

        # Adding model 'TblLocais'
        db.create_table('tbl_locais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local', self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblLocais'])

        # Adding model 'TblApetrechos'
        db.create_table('tbl_apetrechos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apetrecho', self.gf('django.db.models.fields.CharField')(unique=True, max_length='100')),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length='150', blank=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length='250', blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblApetrechos'])

        # Adding model 'TblMetodos'
        db.create_table('tbl_metodos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metodo', self.gf('django.db.models.fields.CharField')(unique=True, max_length='100')),
            ('local', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblLocais'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('var_biodiv', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('var_esforco', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblMetodos'])

        # Adding model 'TblAtrEts'
        db.create_table('tbl_atr_ets', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medida', self.gf('django.db.models.fields.CharField')(unique=True, max_length='100')),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length='150', blank=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblAtrEts'])

        # Adding model 'TblInstrumentais'
        db.create_table('tbl_instrumentais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apetrecho', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblApetrechos'])),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblAtribs'])),
            ('unidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblUnidades'], blank=True)),
            ('valor', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblInstrumentais'])

        # Adding model 'TblMetIns'
        db.create_table('tbl_metins', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metodo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblMetodos'])),
            ('apetrecho', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblApetrechos'])),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('grmetodos', ['TblMetIns'])

        # Adding model 'TblMetAtEts'
        db.create_table('tbl_metatets', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metodo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblMetodos'])),
            ('atributo_estacao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblAtrEts'], blank=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblAtribs'], null=True, blank=True)),
            ('unidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grmetodos.TblUnidades'], null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grmetodos', ['TblMetAtEts'])


    def backwards(self, orm):
        
        # Deleting model 'TblAtribs'
        db.delete_table('tbl_atribs')

        # Deleting model 'TblUnidades'
        db.delete_table('tbl_unidades')

        # Deleting model 'TblLocais'
        db.delete_table('tbl_locais')

        # Deleting model 'TblApetrechos'
        db.delete_table('tbl_apetrechos')

        # Deleting model 'TblMetodos'
        db.delete_table('tbl_metodos')

        # Deleting model 'TblAtrEts'
        db.delete_table('tbl_atr_ets')

        # Deleting model 'TblInstrumentais'
        db.delete_table('tbl_instrumentais')

        # Deleting model 'TblMetIns'
        db.delete_table('tbl_metins')

        # Deleting model 'TblMetAtEts'
        db.delete_table('tbl_metatets')


    models = {
        'grmetodos.tblapetrechos': {
            'Meta': {'object_name': 'TblApetrechos', 'db_table': "'tbl_apetrechos'"},
            'apetrecho': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'100'"}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': "'150'", 'blank': 'True'})
        },
        'grmetodos.tblatrets': {
            'Meta': {'object_name': 'TblAtrEts', 'db_table': "'tbl_atr_ets'"},
            'descricao': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medida': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'100'"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': "'150'", 'blank': 'True'})
        },
        'grmetodos.tblatribs': {
            'Meta': {'object_name': 'TblAtribs', 'db_table': "'tbl_atribs'"},
            'descricao': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medida': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'100'"}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'150'"})
        },
        'grmetodos.tblinstrumentais': {
            'Meta': {'object_name': 'TblInstrumentais', 'db_table': "'tbl_instrumentais'"},
            'apetrecho': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblApetrechos']"}),
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblAtribs']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'unidade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblUnidades']", 'blank': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'grmetodos.tbllocais': {
            'Meta': {'object_name': 'TblLocais', 'db_table': "'tbl_locais'"},
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'})
        },
        'grmetodos.tblmetatets': {
            'Meta': {'object_name': 'TblMetAtEts', 'db_table': "'tbl_metatets'"},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblAtribs']", 'null': 'True', 'blank': 'True'}),
            'atributo_estacao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblAtrEts']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblMetodos']"}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'unidade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblUnidades']", 'null': 'True', 'blank': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'grmetodos.tblmetins': {
            'Meta': {'object_name': 'TblMetIns', 'db_table': "'tbl_metins'"},
            'apetrecho': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblApetrechos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['grmetodos.TblMetodos']"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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
        },
        'grmetodos.tblunidades': {
            'Meta': {'object_name': 'TblUnidades', 'db_table': "'tbl_unidades'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'blank': 'True'}),
            'dimensao': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'esp_tem': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'unidade': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'100'"})
        }
    }

    complete_apps = ['grmetodos']
