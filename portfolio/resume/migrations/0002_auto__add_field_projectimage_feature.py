# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProjectImage.feature'
        db.add_column(u'resume_projectimage', 'feature',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProjectImage.feature'
        db.delete_column(u'resume_projectimage', 'feature')


    models = {
        u'resume.client': {
            'Meta': {'object_name': 'Client'},
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume.Industry']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'resume.industry': {
            'Meta': {'object_name': 'Industry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume.Client']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume.ProjectImage']", 'symmetrical': 'False', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['resume.Technology']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feature': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.technology': {
            'Meta': {'object_name': 'Technology'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['resume']