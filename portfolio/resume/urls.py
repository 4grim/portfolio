from django.conf.urls import patterns, url

from resume.views import index, cv


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^resume/$', cv, name='resume'),
)