from django.shortcuts import render, get_object_or_404, redirect
from upload_post.models import Post
from django.contrib import messages
from .models import Comments
# Create your views here.


def comment(request, post_id): 
    if request.method == "POST": 
        if 'comment_form' in request.POST: 
            comment = request.POST['comment']
            post = get_object_or_404(Post, id=post_id)

            commented, created = Comments.objects.get_or_create(post=post, user=request.user)

            if created: 
                new_comment = Comments.objects.create(
                    user =  request.user , 
                    post = post, 
                    comment = comment
                )
                new_comment.save()
                messages.success(request, 'successfully commented ')
                return redirect('index')
            if commented: 
                messages.success(request, 'you have already commented on this post')
                return redirect('index')

            
    return render(request, 'pages/index.html')