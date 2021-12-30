from django.db import models
from django.db.models.deletion import SET_NULL
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        """String for representing a model object"""
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cover = models.ImageField(null=True, blank=True )


    def __str__(self):
        """String for representing a model object"""
        return self.title

    @property
    def coverURL(self):
        try:
            url = self.cover.url
        except:
            url = ''
        return url

    #def save(self, *args, **kwargs): # new
     #   if not self.slug:
      #      self.slug = slugify(self.title)
       # return super().save(*args, **kwargs)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)