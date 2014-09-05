from django.shortcuts import render
from resume.models import Technology, Industry, Client, Project, ProjectImage


def index(request):
	projects = Project.objects.order_by('-start_date')
	context = {
		'projects': projects,
	}
	return render(request, 'project_index.html', context)

def cv(request):
	projects = Project.objects.order_by('-start_date')
	technologies = Technology.objects.all()
	
	context = {
		'projects': projects,
		'technologies': technologies,
	}
	return render(request, 'resume/cv.html', context)

def project_page(request, title):
	project = Project.objects.get(title=title)
	context = {
		'project': project
	}
	return render(request, 'resume/project_page.html', context)
