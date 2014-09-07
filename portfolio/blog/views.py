import datetime
from django.shortcuts import render
from .models import BlogPost, BlogPostFile, BlogPostImage, Category


def blog_index(request):
	posts = BlogPost.objects.filter(post_date__lte=datetime.datetime.now())
	categories = Category.objects.all()
	context = {
		'posts': posts,
		'categories': categories,
	}
	return render(request, 'blog/blog_index.html', context)

def blog_post(request, slug):
	post = BlogPost.objects.get(slug=slug)
	context =  {
		'post': post,
	}
	return render(request, 'blog/blog_post.html', context)


def blog_category_index(request, slug):
	category = Category.objects.filter(slug=slug)
	context =  {
		'category': category,
	}
	return render(request, 'blog/blog_category_index.html', context)

