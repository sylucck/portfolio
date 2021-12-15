from django.contrib import admin

# Register your models here.
from myblog.models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_on', 'last_modified', 'cover')
    fields = ['title', ('body', 'cover')]

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
