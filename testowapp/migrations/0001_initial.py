# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Avtomobili'
        db.create_table('testowapp_avtomobili', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marka', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('testowapp', ['Avtomobili'])


    def backwards(self, orm):
        # Deleting model 'Avtomobili'
        db.delete_table('testowapp_avtomobili')


    models = {
        'testowapp.avtomobili': {
            'Meta': {'object_name': 'Avtomobili'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marka': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['testowapp']