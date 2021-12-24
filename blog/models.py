from django.db import models
from django.db.models.deletion import SET_NULL
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        """String for representing a model object"""
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    cover = models.ImageField(null=True, blank=True )
    #slug = models.SlugField(max_length=200, null= True, blank=  True, unique=True)
    #status = models.IntegerField(choices=STATUS, default=0)

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