from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth 
from .models import Profile
# Create your views here.

def index(request): 

    return render(request, 'pages/index.html' )

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
                user_model = User.objects.get(username=username)

                new_profile = Profile.objects.create(
                    user = user_model, 
                )
                new_profile.save() 
                return redirect('signup')
        
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
