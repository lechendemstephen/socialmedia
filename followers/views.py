from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Follow
from django.contrib import messages
# Create your views here.
@login_required(login_url='signin')
def follow(request, user_id):
    user_to_follow = get_object_or_404(Follow, id=user_id)

    if user_to_follow != request.user: 
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        messages.success(request, 'follow successfull')
        return redirect('index')



