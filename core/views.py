from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
from .models import Profile
from upload_post.models import Post, LikePost
from Comments.models import Comments 

# Create your views here.
user = get_user_model()


@login_required(login_url='signin')
def index(request): 
    
    user_profile= Profile.objects.get(user=request.user.username)
    comments = Comments.objects.all()
    available_users = User.objects.all()
   
    post = Post.objects.all()

    if request.method == "POST": 
            if 'pic_upload' in request.POST: 
                image = request.FILES.get('image')
                caption = request.POST['caption']
                new_post = Post.objects.create (
                    owner = request.user,
                    user = request.user.username, 
                    img = image, 
                    caption = caption
                )

                new_post.save()
                messages.success(request, 'post successfully')
                return redirect('index')

    context = {
        "user_profile": user_profile,
        "posts": post, 
        "comments": comments,
        "avaiable_users": available_users,
       
    }

    return render(request, 'pages/index.html', context)

@login_required(login_url='signin')
def settings(request): 

    user_profile = Profile.objects.get(user=request.user.username)
   
    if request.method == "POST": 

        if request.FILES.get('image') == None: 
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.user = user.username
            user_profile.profileimg = image
            user_profile.bio = bio 
            user_profile.location = location 
            user_profile.save()
        
        if request.FILES.get('image') != None: 
            image =  request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio 
            user_profile.location = location 
            user_profile.save()

        return redirect('settings')
        
    context = {
        "user_profile": user_profile, 
    }



    return render(request, 'pages/setting.html', context)




def signup(request): 
    if request.method == "POST": 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']

        if password == password2: 
            if User.objects.filter(email=email).exists(): 
                messages.info(request, 'user with email already exist you might want to login')
                return redirect('signup')
            elif User.objects.filter(username=username).exists(): 
                    messages.info(request, 'username taken')
                    return redirect('signup')
            else: 

                user = User.objects.create_user(
                    username=username, 
                    email=email, 
                    password=password
                )
                user.save() 

                # log user in and redirect to settings page 
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)


                user_model = User.objects.get(username=username)

                new_profile = Profile.objects.create(
                    user = user_model.username, 
                )
                new_profile.save() 
                return redirect('settings')
        
        else: 
            messages.error(request, 'password does not match')
            return redirect('signup')


    else: 
      return render(request, 'pages/signup.html' )

def signin(request): 
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'successfully logged in ')
            return redirect('index')
        else: 
            messages.error(request, 'invalid credentials')
            return redirect('signin')
    else: 
     return render(request, 'pages/signin.html')



@login_required(login_url='sigin')
def logout(request): 
    auth.logout(request)

    return redirect('signin')


# liking and unliking post functionality
def like_post(request, post_id): 
    post = get_object_or_404(Post, id=post_id)
    liked, created = LikePost.objects.get_or_create(post=post, user=request.user)
    # checking if the post is just liked or was already liked
    if created: 
        post.no_of_likes = post.no_of_likes + 1 
        post.save()
        messages.success(request, 'successfully liked')
        return redirect('index')
    if liked: 
        post.no_of_likes = post.no_of_likes - 1 
        liked.delete()
        post.save()
        messages.success(request, 'successfully unliked')
        return redirect('index')
    
    context = {
            'likes': post.no_of_likes,
        }


    return render(request, 'pages/index.html', context)


# user profile 
def user_profile(request): 
    user_profile= Profile.objects.get(user=request.user)
    post = Post.objects.filter(user=request.user)
    


    context = {
        "user": user_profile, 
        "posts": post, 
        "no_post":  post.count()
        
    }



    return render(request, 'pages/profile.html', context)
    




