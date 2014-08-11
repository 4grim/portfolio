from django.shortcuts import render


def index(request):
	context = {}
	return render(request, 'index.html', context)


def cv(request):
	context = {}
	return render(request, 'resume/cv.html', context)