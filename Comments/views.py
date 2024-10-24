from django.shortcuts import render, get_object_or_404, redirect
from upload_post.models import Post
from django.contrib import messages
from .models import Comments

# Create your views here.


def comment(request, post_id): 
    if request.method == "POST":
        print('post is working') 
        if 'comment_form' in request.POST: 
            comment = request.POST['comment']
            post = get_object_or_404(Post, id=post_id)
          
            new_comment = Comments.objects.create(
                    user =  request.user , 
                    post = post, 
                    comment = comment
                )
            new_comment.save()
            messages.success(request, 'successfully commented ')
            return redirect('index', post.pk)
        
    return render(request, 'pages/index.html')



def test_comment(request): 
      ...
    # if request.method == "POST":
    #     comment = request.POST['comment'] 
    #     user = request.user

    #     new_comment = TestComment.objects.create(
    #         comment = comment,
    #         user = user
    #     )

    #     new_comment.save()
    #     messages.success(request, 'comment successful')

    #     return redirect('test_comment')
    

    # return render(request, 'pages/test.html')