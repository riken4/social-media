from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .models import Follow
from post.models import Notification



# Create your views here.


def signup_view(request):
    if request.user is authenticate:
        return redirect('home')
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        if password != password2:
            messages.error(request, "Password don't match")
            return redirect('signup')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "email already exist")   
            return redirect('signup')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exist")   
            return redirect('signup')
            
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        login(request, user)
        messages.success(request,'user created successfully')
        return redirect('home')
    return render(request, 'pages/signup.html')

def login_view(request):
    if request.user is authenticate:
        return redirect('home')
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"welcome back, {user.username}")
            return redirect('home')
        else:
            return render(request, 'pages/login.html', {'error':"Invalid username and password"})
    return render(request, 'pages/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'logout successful')
    return redirect('login')

@login_required
def profile_view(request, username):
    profile_user=CustomUser.objects.get(username=username)
    posts=profile_user.posts.all()
    is_following=False
    if Follow.objects.filter(follower=request.user,
                             following=profile_user).exists():
        is_following=True 
    context={'profile_user':profile_user,'posts':posts,'is_following':is_following,'following_count':profile_user.get_following_count(),'followers_count':profile_user.get_followers_count()}
    return render(request,'components/base.html',context)

@login_required
def edit_profile_view(request):
    return render(request,'pages/edit_profile.html')

def edit_post(request, username):
    if request.method =="POST":
        user=request.user
        bio=request.POST.get("bio")
        location=request.POST.get("location")
        profile_picture=request.FILES.get("profile_photo")
        user.bio=bio
        user.location=location
        user.profile_picture=profile_picture
        user.save()
        messages.success(request,'updated successfully')
    return redirect('profile',username=username)


# create my profile
#  user=request.user
# follower following count
# post counts


@login_required
def follow_toggle(request, username):
    if request.method=='POST':
        user_to_follow=CustomUser.objects.get(username=username)
        if request.user==user_to_follow:
            messages.error(request, 'you cannot follow yourself')
            return redirect('profile',username=username)
        follow_instance=Follow.objects.filter(
            follower=request.user,
            following=user_to_follow
            ).first()
        if follow_instance:
            follow_instance.delete()
            messages.success(request, f"you unfollowed {username}")
        else:
            Follow.objects.create(follower=request.user,following=user_to_follow)
            messages.success(request, f"you followed {username}")
            Notification.objects.create(
                recipient=user_to_follow,
                sender=request.user,
                notification_type='follow')
        return redirect('profile',username=username)
    return redirect('home')

