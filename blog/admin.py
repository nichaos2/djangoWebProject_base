"""
author: nichaos2
date: 24/08/2021

Adding Models To The Administration Site
----------------------------------------

after having the default functionallity the class PostAdmin is created to enhance it

Code copied from the site https://djangocentral.com/building-a-blog-application-with-django/
"""

from django.contrib import admin

# Register your models here.
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    """
    Diplays the post a bit better than the default
    """
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)} # creates the slug content based on the title

admin.site.register(Post, PostAdmin)