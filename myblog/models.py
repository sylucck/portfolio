from django.db import models

# Create your models here.
#class Image(models.Model):
   # title = models.CharField(max_length=200, default=None, blank=False, null=False)
    #image_cov = models.ImageField(null=True, blank=True )

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
    cover = models.ImageField(null=True, blank=True)
    #status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        """String for representing a model object"""
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)