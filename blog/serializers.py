"""
author: nichaos2
date: 24/08/2021

Create serializer
-----------------

see in the tutorial https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

"""

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author', 'updated_on', 'content', 'content', 'created_on', 'status')