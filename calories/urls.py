from django.urls import path
from . import views


urlpatterns = [
    path('calories/', views.HomePageView, name="calories"),

]