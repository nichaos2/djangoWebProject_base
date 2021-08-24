"""
Adding Models To The Administration Site
Code copied from the site https://djangocentral.com/building-a-blog-application-with-django/
"""

from django.contrib import admin

# Register your models here.
from .models import Post 

admin.site.register(Post)