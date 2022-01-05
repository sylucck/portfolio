from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Food)
admin.site.register(Food_Profile)