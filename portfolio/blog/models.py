from django.db import models


class Category(models.Model):
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class BlogPostImage(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, default='default')
	image = models.ImageField(upload_to='blog', blank=True)
	feature_image = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title


class BlogPostFile(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	slug = models.SlugField(unique=True, default='default')
	entry_file = models.FileField(upload_to='blog', blank=True)

	def __unicode__(self):
		return self.title


class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.TextField(max_length=500, blank=True)
	post_date = models.DateTimeField()
	text = models.TextField()
	slug = models.SlugField(unique=True)
	categories = models.ManyToManyField(Category, blank=True)
	images = models.ManyToManyField(BlogPostImage, blank=True)
	files = models.ManyToManyField(BlogPostFile, blank=True)

	def __unicode__(self):
		return self.title



