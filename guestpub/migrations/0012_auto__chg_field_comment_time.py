# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Comment.time'
        db.alter_column(u'guestpub_comment', 'time', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Comment.time'
        db.alter_column(u'guestpub_comment', 'time', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'guestpub.comment': {
            'Meta': {'unique_together': "(('pub', 'comment_id'),)", 'object_name': 'Comment'},
            'comment_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'num_rate': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'pub': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guestpub.Pub']"}),
            'time': ('django.db.models.fields.DateField', [], {})
        },
        u'guestpub.message': {
            'Meta': {'object_name': 'Message'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'num_children': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'num_men': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'num_women': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'receiver_tel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'result': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender_tel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'})
        },
        u'guestpub.pub': {
            'Meta': {'ordering': "['-imageurl']", 'object_name': 'Pub'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'placeurl': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0 0)'", 'blank': 'True'}),
            'refer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'})
        },
        u'guestpub.publistplugin': {
            'Meta': {'object_name': 'PubListPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['guestpub']