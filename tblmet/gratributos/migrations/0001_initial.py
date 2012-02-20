# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TblAtributos'
        db.create_table('tbl_atributos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_valor', self.gf('django.db.models.fields.CharField')(max_length='1')),
            ('no_at_ca_co', self.gf('django.db.models.fields.CharField')(max_length='40')),
            ('legenda', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length='1')),
            ('unidade_utilizada', self.gf('django.db.models.fields.CharField')(max_length='60')),
        ))
        db.send_create_signal('gratributos', ['TblAtributos'])


    def backwards(self, orm):
        
        # Deleting model 'TblAtributos'
        db.delete_table('tbl_atributos')


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
        }
    }

    complete_apps = ['gratributos']
