from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Like,Post,Comment
from django.contrib import messages
from post.models import Notification
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationSerializer 
#notification serializer
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

@login_required
def home_veiw(request):
    post=Post.objects.all().order_by('-created_at')
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
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        like_instance=Like.objects.filter(user=request.user,post=post)
        if like_instance:
            like_instance.delete()
        else:
            like_instance=Like.objects.create(user=request.user,post=post)
        if post.auther!=request.user:  
            Notification.objects.create(recipient=post.auther,sender=request.user,notification_type='like',post=post)
            messages.SUCCESS(request,'like added sucessfully')
        return redirect('home')
    return redirect('home')

@login_required
def add_comment(request, post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        content=request.POST.get('content')
        comment=Comment.objects.create(
            post=post,
            cotent=content
        )
        if post.author!=request.user:
            Notification.objects.create(recieipent=post.author,sender=request.user,notification_type='comment',post=post,comment=comment)
            messages.SUCCESS(request,'comment added sucessfully')
        return redirect('home')
    return redirect('home')

@login_required
def delete_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    comment.delete()
    messages.SUCCESS(request,'comment deleted successfully')
    return redirect('home')


class notification_api_view(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        notification=notification.objects.filter(reciepient=request.user)
        serializer=NotificationSerializer (notification,mean=True)
        unread_count = Notification.objects.filter(recipient=request.user, is_read=False).count()
        return Response({
            'notification':serializer.data,
            'unread_count':unread_count,
        })
    
class mark_notification_read_api_view(APIView):
    permission_classes=[IsAuthenticated]
    def post(Self,request,notification_id):
        notification=Notification.objects.get(id=notification_id)    
        notification.is_read=True
        notification.save()
        return Response({'status':'sucess'})

class mark_all_notification_read_api_view(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,reques):
        notification=Notification.objects.filter(receipeial=reques.user,is_read=False).update(is_read=True)
        return Response({'status':'sucess'})
        



#forgetpassword page
# otp page
# update password page
#email otp
# 1 page forgett.py- button click-
# setting.py
#reset password

