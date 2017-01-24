from django.conf.urls import url

from .views import main_page, blog_page

urlpatterns = [
				url(r'^$', main_page, name = 'main_page'),
				url(r'^blog-page/$', blog_page, name = 'blog_page'),
				]