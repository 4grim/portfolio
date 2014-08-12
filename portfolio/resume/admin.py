from django.contrib import admin
from resume.models import Technology, Industry, Client, Project, ProjectImage


admin.site.register(Technology)
admin.site.register(Industry)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(ProjectImage)
