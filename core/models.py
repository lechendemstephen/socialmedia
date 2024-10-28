from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model): 
    user = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profileimg  = models.ImageField(upload_to='profile_images/', default='default_profile.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self): 

        return self.user.username 
    
