from django.conf.urls import patterns, url

from resume.views import index, cv, project_index


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^resume/$', cv, name='resume'),
    url(r'^projects/$', project_index, name="project_index")
)