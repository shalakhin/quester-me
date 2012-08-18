# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table('quest_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('quest', ['Address'])

        # Adding model 'Marker'
        db.create_table('quest_marker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quest.Quest'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quest.Address'])),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('quest', ['Marker'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table('quest_address')

        # Deleting model 'Marker'
        db.delete_table('quest_marker')


    models = {
        'quest.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'quest.marker': {
            'Meta': {'object_name': 'Marker'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quest.Address']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quest.Quest']"})
        },
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