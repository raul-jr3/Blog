from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Blog

def main_page(request):
	return render(request, 'blog/main_page.html')

def blog_page(request):
	user = User.objects.all()
	posts = Blog.objects.all()
	return render(request, 'blog/blog_page.html', {'posts' : posts})