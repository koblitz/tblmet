# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TblEmpreendimentos'
        db.create_table(u'tbl_empreendimentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('num_processo', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grempres', ['TblEmpreendimentos'])

        # Adding model 'TblEmpresas'
        db.create_table(u'tbl_empresas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empreendimento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grempres.TblEmpreendimentos'], blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal('grempres', ['TblEmpresas'])

        # Adding model 'TblPessoas'
        db.create_table(u'tbl_pessoas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['grempres.TblEmpresas'], blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='CPF', blank=True)),
            ('link_lattes', self.gf('django.db.models.fields.URLField')(max_length=80, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50, blank=True)),
            ('telefone_princ', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('telefone_sec', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('grempres', ['TblPessoas'])


    def backwards(self, orm):
        
        # Deleting model 'TblEmpreendimentos'
        db.delete_table(u'tbl_empreendimentos')

        # Deleting model 'TblEmpresas'
        db.delete_table(u'tbl_empresas')

        # Deleting model 'TblPessoas'
        db.delete_table(u'tbl_pessoas')


    models = {
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
        }
    }

    complete_apps = ['grempres']
