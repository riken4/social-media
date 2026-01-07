from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Like,Post
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

@login_required
def home_veiw(request):
    post=request.objects.all().order_by('-created_at')
    like_obj=Like.objects.filter(user=request.user)
    user_like=like_obj.values_list('post_id',flat=True)
    context={
        'posts':post,
        'user_likes':user_like
    }
    return render(request,'pages/home.html',context)

@login_required
def create_post(request):
    if request.method=='POST':
        content=request.get('content')
        image=request.FILES.get('image_url')
        if content:
            post=Post.objects.create(
                content=content,
                image=image
            )
            messages.SUCCESS(request,'post created successfully')
        else:
            messages.error(request,'content cannot be empty')
        return redirect('home') 
    return redirect('home')

@login_required
def edit_post(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method =="POST":
        content=request.POST.get("content")
        post.content=content
        post.is_edited=True
        post.save()
        messages.SUCCESS(request,'post updated successfully')
        return redirect('home')
    return render(request,'pages/edit_post.html',{'post':post})

@login_required
def delete_post(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method=="POST":
        post.delete()
        messages.SUCCESS(request,'post deleted successfully')
        return redirect('home')
    return render(request,'pages/edit_post.html',{'post':post})


#like post function
#def like_post
@login_required
def like_post(request,post_id):