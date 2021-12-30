from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    
    #if request.method == 'POST':
     #   form = SearchForm(request.POST)
      #  if form.is_valid():
       #     title_search = form.cleaned_data['title_search']
        #    blog = Post.objects.get(title=title_search)
         #   return redirect(f'/blog/<pk>')
    #else:
     #   form = SearchForm()
    context = {
        "posts": posts,
        
        #'form': form
        }
    return render(request, 'blog/blog_index.html', context)



def blog_details(request, slug):
    post = Post.objects.get(slug = slug)
    comments = Comment.objects.filter(post=post)
    


    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    context = {
        "post": post,
        "comments": comments,
        "form": form,
        
    }
    return render(request, "blog/blog_details.html",  context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/blog_category.html", context)