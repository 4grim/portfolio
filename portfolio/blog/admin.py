from django.contrib import admin
from .models import BlogPost, BlogPostFile, BlogPostImage, Category

class BlogPostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


class BlogPostImageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


class BlogPostFileAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostImage, BlogPostImageAdmin)
admin.site.register(BlogPostFile, BlogPostFileAdmin)
admin.site.register(Category)
