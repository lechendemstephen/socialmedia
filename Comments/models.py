from django.db import models
from django.contrib.auth.models import User
from upload_post.models import Post

# Create your models here.

class Comments(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.PositiveBigIntegerField(default=0)


    def __str__(self): 

        return self.comment
    

    class Meta: 
        verbose_name_plural = 'Comments'


class TestComment(models.Model): 
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self): 

        return self.comment