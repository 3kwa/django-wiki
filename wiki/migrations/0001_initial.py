# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table('wiki_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('wiki', ['Page'])

        # Adding model 'Edit'
        db.create_table('wiki_edit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wiki.Page'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wiki', ['Edit'])

    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table('wiki_page')

        # Deleting model 'Edit'
        db.delete_table('wiki_edit')

    models = {
        'wiki.edit': {
            'Meta': {'object_name': 'Edit'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiki.Page']"})
        },
        'wiki.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['wiki']