from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('title',)}
	list_display = ['title', 'created', 'updated', 'author']

admin.site.register(Blog, BlogAdmin)