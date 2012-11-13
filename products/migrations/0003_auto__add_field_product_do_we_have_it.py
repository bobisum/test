# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.do_we_have_it'
        db.add_column('products_product', 'do_we_have_it',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.do_we_have_it'
        db.delete_column('products_product', 'do_we_have_it')


    models = {
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'do_we_have_it': ('django.db.models.fields.CharField', [], {'default': "'IS'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['products']