from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

# @login_required(login_url='signin')
# def upload(request):
#         if request.method == "POST": 
#             user = User.username
#             image = request.FILES.get('image_upload')
#             caption = request.POST['caption']

#             new_post = Post.objects.create(
#                 user = user, 
#                 image = image, 
#                 caption = caption
#             )
#             new_post.save()
#             messages.success(request, 'post successfully')
          
#         return render(request, 'pages/index.html', )