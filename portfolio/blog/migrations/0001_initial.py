# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding model 'BlogPostImage'
        db.create_table(u'blog_blogpostimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='default', unique=True, max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('feature_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'blog', ['BlogPostImage'])

        # Adding model 'BlogPostFile'
        db.create_table(u'blog_blogpostfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='default', unique=True, max_length=50)),
            ('entry_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'blog', ['BlogPostFile'])

        # Adding model 'BlogPost'
        db.create_table(u'blog_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subtitle', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'blog', ['BlogPost'])

        # Adding M2M table for field categories on 'BlogPost'
        m2m_table_name = db.shorten_name(u'blog_blogpost_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogpost', models.ForeignKey(orm[u'blog.blogpost'], null=False)),
            ('category', models.ForeignKey(orm[u'blog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blogpost_id', 'category_id'])

        # Adding M2M table for field images on 'BlogPost'
        m2m_table_name = db.shorten_name(u'blog_blogpost_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogpost', models.ForeignKey(orm[u'blog.blogpost'], null=False)),
            ('blogpostimage', models.ForeignKey(orm[u'blog.blogpostimage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blogpost_id', 'blogpostimage_id'])

        # Adding M2M table for field files on 'BlogPost'
        m2m_table_name = db.shorten_name(u'blog_blogpost_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogpost', models.ForeignKey(orm[u'blog.blogpost'], null=False)),
            ('blogpostfile', models.ForeignKey(orm[u'blog.blogpostfile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blogpost_id', 'blogpostfile_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Deleting model 'BlogPostImage'
        db.delete_table(u'blog_blogpostimage')

        # Deleting model 'BlogPostFile'
        db.delete_table(u'blog_blogpostfile')

        # Deleting model 'BlogPost'
        db.delete_table(u'blog_blogpost')

        # Removing M2M table for field categories on 'BlogPost'
        db.delete_table(db.shorten_name(u'blog_blogpost_categories'))

        # Removing M2M table for field images on 'BlogPost'
        db.delete_table(db.shorten_name(u'blog_blogpost_images'))

        # Removing M2M table for field files on 'BlogPost'
        db.delete_table(db.shorten_name(u'blog_blogpost_files'))


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.BlogPostFile']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.BlogPostImage']", 'symmetrical': 'False', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.blogpostfile': {
            'Meta': {'object_name': 'BlogPostFile'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'entry_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'default'", 'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.blogpostimage': {
            'Meta': {'object_name': 'BlogPostImage'},
            'feature_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'default'", 'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']