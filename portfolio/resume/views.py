from django.shortcuts import render
from resume.models import Technology, Industry, Client, Project, ProjectImage


def index(request):
	context = {}
	return render(request, 'index.html', context)


def cv(request):
	projects = Project.objects.order_by('-start_date')
	technologies = Technology.objects.all()
	context = {
		'projects': projects,
		'technologies': technologies,
	}
	return render(request, 'resume/cv.html', context)