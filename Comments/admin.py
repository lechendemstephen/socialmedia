from django.contrib import admin
from .models import Comments, TestComment
# Register your models here.


class CommentsAdmin(admin.ModelAdmin): 
    list_display = ('user', 'comment', 'post')


admin.site.register(TestComment)
admin.site.register(Comments, CommentsAdmin)

