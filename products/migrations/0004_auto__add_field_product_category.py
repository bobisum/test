# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.category'
        db.add_column('products_product', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['category.Category'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.category'
        db.delete_column('products_product', 'category_id')


    models = {
        'category.category': {
            'Meta': {'object_name': 'Category'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['category.Category']", 'null': 'True'}),
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