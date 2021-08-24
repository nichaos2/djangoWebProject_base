"""
author: nichaos2
date: 24/08/2021

Building Views
--------------

Class-based views - we need to create an HTML template for the data returned from the views.

The built-in ListViews which is a subclass of generic class-based-views render a list with the objects of the 
specified model we just need to mention the template, similarly DetailView provides a detailed view for a 
given object of the model at the provided template.

Code copied from the site https://djangocentral.com/building-a-blog-application-with-django/
"""

from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    """[summary]

    Args:
        generic ([type]): [description]

    Notice that filte status=1 shows only the published posts
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'