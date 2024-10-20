from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin): 
    list_display = ('user', 'caption', 'created_at', 'no_of_likes')



admin.site.register(Post, PostAdmin)