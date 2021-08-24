"""
author: nichaos2
date: 24/08/2021

URL patterns for Views
----------------------

map URLs for each view 

When a user makes a request for a page on your web app,
the Django controller takes over to look for the corresponding
view via the urls.py file, and then return the HTML response
or a 404 not found error, if not found.

Code copied from the site https://djangocentral.com/building-a-blog-application-with-django/
"""

from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]