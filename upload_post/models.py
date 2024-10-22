from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User
import uuid 

User = get_user_model()


# Create your models here.
class Post(models.Model): 
    user = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='profile_images/', blank=True)
    caption = models.TextField(blank=True, max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.PositiveBigIntegerField(default=0)


    @property 
    def image_url(self): 
        if self.img and hasattr(self.img, 'url'): 
            return self.img.url 


    def __str__(self): 

        return self.user
    
class LikePost(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    def __str__(self):

        return self.user.username
    
    

