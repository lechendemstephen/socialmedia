from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
from .models import Profile
from upload_post.models import Post
# Create your views here.

user = get_user_model()

@login_required(login_url='signin')
def index(request): 
    user_object = User.objects.get(username=request.user.username)
    user_profile= Profile.objects.get(user=user_object)
    post = Post.objects.all()

    if request.method == "POST": 
            image = request.FILES.get('image')
            caption = request.POST['caption']
            new_post = Post.objects.create (
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
    }

    return render(request, 'pages/index.html', context)

@login_required(login_url='signin')
def settings(request): 
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST": 

        if request.FILES.get('image') == None: 
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

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
                    user = user_model, 
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
