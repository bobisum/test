# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Categorys'
        db.delete_table('category_categorys')

        # Adding model 'Category'
        db.create_table('category_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('category', ['Category'])


    def backwards(self, orm):
        # Adding model 'Categorys'
        db.create_table('category_categorys', (
            ('category', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('category', ['Categorys'])

        # Deleting model 'Category'
        db.delete_table('category_category')


    models = {
        'category.category': {
            'Meta': {'object_name': 'Category'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['category']