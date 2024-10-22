from django.contrib import admin
from .models import Comments
# Register your models here.


class CommentsAdmin(admin.ModelAdmin): 
    list_display = ('user', 'comment', 'post')


admin.site.register(Comments, CommentsAdmin)
