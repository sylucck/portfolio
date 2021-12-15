from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"), #homepage of the blog
    path("myblog/", views.myblog_index, name="myblog_index"), #myblog page of the blog
    path("myblog/<int:pk>/", views.myblog_details, name="myblog_detail"), #myblog details page of myblog page
    path("myblog/<category>/", views.myblog_category, name="myblog_category"),  #myblog category page
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)



