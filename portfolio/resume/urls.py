from django.conf.urls import patterns, url

from resume.views import index, cv, project_page


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^resume/$', cv, name='resume'),
    url(r'^projects/(?P<title>[a-zA-Z0-9-_]+)/$', project_page, name='project_page'),
)