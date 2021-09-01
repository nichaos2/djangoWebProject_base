
"""
author: nichaos2
date: 01/09/2021

Register and Login views
------------------------

Code created from https://www.youtube.com/watch?v=Ev5xgwndmfc&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9&index=9&ab_channel=TechWithTim
"""

from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    template_name = 'registration/register.html'

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, template_name, {"form":form} )