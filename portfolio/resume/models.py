from django.db import models


class Technology(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Industry(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Client(models.Model):
	name = models.CharField(max_length=200)
	website = models.URLField()
	email = models.EmailField(max_length=254, blank=True)
	contact_person = models.CharField(max_length=200, blank=True)
	industries = models.ManyToManyField(Industry)

	def __unicode__(self):
		return self.name


class ProjectImage(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='resume')

	def __unicode__(self):
		return self.title


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	client = models.ForeignKey(Client)
	images = models.ManyToManyField(ProjectImage, blank=True)
	start_date = models.DateField()
	end_date = models.DateField()
	position = models.CharField(max_length=200)
	technologies = models.ManyToManyField(Technology)

	def __unicode__(self):
		return self.title






