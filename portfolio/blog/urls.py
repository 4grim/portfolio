from django.conf.urls import patterns, url

from blog.views import blog_index


urlpatterns = patterns('',
    url(r'^$', blog_index, name='blog_index'),
)