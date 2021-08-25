"""
author: nichaos2
date: 25/08/2021

Adding Forms
------------

Djang API to handle forms, since the form input will be saved in the database models

Code copied from the site https://djangocentral.com/creating-comments-system-with-django/
"""

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')