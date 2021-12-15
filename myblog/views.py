from django.shortcuts import render
from .forms import CommentForm


# Create your views here.
from myblog.models import Post, Comment

def home(request):
    return render(request, 'home.html')


def myblog_index(request):
    return render(request, 'myblog/myblog_index.html')

def myblog_details(request):
    return render(request, "myblog/myblog_details.html")

def myblog_category(request):
    return render(request, "myblog/myblog_category.html")