from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import *

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    summernote_fields = ('content',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

