# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Technology'
        db.create_table(u'resume_technology', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Technology'])

        # Adding model 'Industry'
        db.create_table(u'resume_industry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Industry'])

        # Adding model 'Client'
        db.create_table(u'resume_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'resume', ['Client'])

        # Adding M2M table for field industries on 'Client'
        m2m_table_name = db.shorten_name(u'resume_client_industries')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('client', models.ForeignKey(orm[u'resume.client'], null=False)),
            ('industry', models.ForeignKey(orm[u'resume.industry'], null=False))
        ))
        db.create_unique(m2m_table_name, ['client_id', 'industry_id'])

        # Adding model 'ProjectImage'
        db.create_table(u'resume_projectimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'resume', ['ProjectImage'])

        # Adding model 'Project'
        db.create_table(u'resume_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.Client'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Project'])

        # Adding M2M table for field images on 'Project'
        m2m_table_name = db.shorten_name(u'resume_project_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'resume.project'], null=False)),
            ('projectimage', models.ForeignKey(orm[u'resume.projectimage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'projectimage_id'])

        # Adding M2M table for field technologies on 'Project'
        m2m_table_name = db.shorten_name(u'resume_project_technologies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'resume.project'], null=False)),
            ('technology', models.ForeignKey(orm[u'resume.technology'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'technology_id'])


    def backwards(self, orm):
        # Deleting model 'Technology'
        db.delete_table(u'resume_technology')

        # Deleting model 'Industry'
        db.delete_table(u'resume_industry')

        # Deleting model 'Client'
        db.delete_table(u'resume_client')

        # Removing M2M table for field industries on 'Client'
        db.delete_table(db.shorten_name(u'resume_client_industries'))

        # Deleting model 'ProjectImage'
        db.delete_table(u'resume_projectimage')

        # Deleting model 'Project'
        db.delete_table(u'resume_project')

        # Removing M2M table for field images on 'Project'
        db.delete_table(db.shorten_name(u'resume_project_images'))

        # Removing M2M table for field technologies on 'Project'
        db.delete_table(db.shorten_name(u'resume_project_technologies'))


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