from typing import List
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Post

# Create your views here.
class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "index.html"
    # model = Post this is a shortcut to Post.objects.all()
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[:30]

