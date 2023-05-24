from django.contrib import admin

from .models import *


# class ImageInline(admin.StackedInline):
#     model=Image

# class PostsAdmin(admin.ModelAdmin):
#     inlines = [ImageInline]

admin.site.register(Posts)