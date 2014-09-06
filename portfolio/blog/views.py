import datetime
from django.shortcuts import render
from .models import BlogPost, BlogPostFile, BlogPostImage, Category


def blog_index(request):
	posts = BlogPost.objects.filter(post_date__lte=datetime.datetime.now())
	context = {
		'posts': posts,
	}
	return render(request, 'blog/blog_index.html', context)
