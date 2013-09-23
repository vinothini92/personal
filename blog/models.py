from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
	author = models.CharField(max_length=30)
	title = models.CharField(max_length=200)
	body = models.TextField()

	def __unicode__(self):
		return self.title

class PostAdmin(admin.ModelAdmin):
	list_display=('title','body')

