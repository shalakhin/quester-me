# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quest'
        db.create_table('quest_quest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('difficulty_level', self.gf('django.db.models.fields.CharField')(default='0', max_length=2, blank=True)),
        ))
        db.send_create_signal('quest', ['Quest'])


    def backwards(self, orm):
        # Deleting model 'Quest'
        db.delete_table('quest_quest')


    models = {
        'quest.quest': {
            'Meta': {'object_name': 'Quest'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'difficulty_level': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['quest']