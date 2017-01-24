from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField(max_length = 90)
	slug = models.SlugField(unique = True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(User)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title