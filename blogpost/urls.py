from django.urls import path

from . import views


urlpatterns = [
    #Leave as empty string for base url
	path('', views.home, name="home"),
    path("blog/", views.blog_index, name="blog_index"), #myblog page of the blog
    path("blog/<slug:slug>/", views.blog_details, name="blog_details"), #myblog details page of myblog page
    path("blog/<category>/", views.blog_category, name="blog_category"),  #myblog category page
	
]