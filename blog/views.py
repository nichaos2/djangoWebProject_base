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

Add a view to see the API from the tutorial in https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
"""

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from .models import Post
from .forms import CommentForm

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from blog import serializers


class PostList(generic.ListView):
    """[summary]

    Args:
        generic ([type]): [description]

    Notice that filte status=1 shows only the published posts
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class PostApiView(viewsets.ModelViewSet):
    """ class to see the APi """
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('created_on')
    lookup_field = 'slug'

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List' : '/post-list/',
        'Detail View' : '/post-detail/<str:ok>/',
        'Create' : '/post-create/',
        'Update' : '/post-update/<str:pk>/',
        'Delete' : '/post-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
