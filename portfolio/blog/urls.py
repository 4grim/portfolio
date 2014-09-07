from django.conf.urls import patterns, url

from blog.views import blog_index, blog_post, blog_category_index


urlpatterns = patterns('',
    url(r'^$', blog_index, name='blog_index'),
    url(r'^category/(?P<slug>[a-zA-Z0-9-_ ]+)/$', blog_category_index, name='blog_category_index'),
    url(r'^(?P<slug>[a-zA-Z0-9-_]+)/$', blog_post, name='blog_post'),
)