import datetime
from django.shortcuts import render
from .models import BlogPost, BlogPostFile, BlogPostImage, Category

def blog_context(request):
	published_posts = BlogPost.objects.filter(post_date__lte=datetime.datetime.now())
	categories = Category.objects.all()
	context = {
		'published_posts': published_posts,
		'categories': categories,
	}
	return context


def blog_index(request):
	context = blog_context(request)
	return render(request, 'blog/blog_index.html', context)


def blog_post(request, slug):
	context = blog_context(request)
	post = BlogPost.objects.get(slug=slug)
	context['post'] = post
	return render(request, 'blog/blog_post.html', context)


def blog_category_index(request, slug):
	context = blog_context(request)
	category = Category.objects.get(slug=slug)
	category_posts = BlogPost.objects.filter(post_date__lte=datetime.datetime.now(), categories__title=category)
	context['category'] = category
	context['category_posts'] = category_posts
	return render(request, 'blog/blog_category_index.html', context)

