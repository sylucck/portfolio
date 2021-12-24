from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')

    context = {
        "posts": posts,  
        }
    return render(request, 'blog/blog_index.html', context)


def blog_details(request):
    return render(request, "blog/blog_details.html")

def blog_category(request):
    return render(request, "blog/blog_category.html")