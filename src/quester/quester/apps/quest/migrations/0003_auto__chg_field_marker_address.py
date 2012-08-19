# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Marker.address'
        db.alter_column('quest_marker', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quest.Address'], null=True))

    def backwards(self, orm):

        # Changing field 'Marker.address'
        db.alter_column('quest_marker', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['quest.Address']))

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
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quest.Address']", 'null': 'True', 'blank': 'True'}),
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