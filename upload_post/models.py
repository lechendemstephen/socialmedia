from django.db import models
from django.contrib.auth import get_user_model 
import uuid 

User = get_user_model()


# Create your models here.
class Post(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='profile_images/', blank=True)
    caption = models.TextField(blank=True, max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)


    @property 
    def image_url(self): 
        if self.img and hasattr(self.img, 'url'): 
            return self.img.url 


    def __str__(self): 

        return self.user
    
    

