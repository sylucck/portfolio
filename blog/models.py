from django.db import models
from django.db.models.deletion import SET_NULL


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

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)