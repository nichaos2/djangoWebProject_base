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
from django.urls import path, include

from rest_framework import routers

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r"posts", views.PostApiView, "posts")

# add blog in from of the following urls
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("api/", include(router.urls), name="api"),
    path("api_overview/", views.api_overview, name="api_overview"),
    path("api_overview/post-list/", views.postList, name="post-list"),
    path(
        "openapi/",
        get_schema_view(
            title="Blog Posts service",
            description="API to get the post of the nichaos blog",
        ),
        name="openapi-schema",
    ),
    path("swagger/", get_swagger_view(title="Swagger Blog Posts service"), name="swagger"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
