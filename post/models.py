from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Post(models.Model):
    auther=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post')
    content=models.TextField(max_length=255)
    image=models.ImageField(upload_to='post_image/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited=models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.auther.username}"

class Like(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_like')
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f"{self.user.username} like {self.post.id}"


class Comment(models.Model):
    post=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='user_comments')
    content=models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
          return f"{self.author.username} comments on{self.post.id}"

class Notification(models.Model):
    NOTIFICATION_TYPES=(
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow')
    )
    recipient=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notification')
    sender=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notification')
    notification_type=models.CharField(max_length=255, choices=NOTIFICATION_TYPES)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    is_read=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.notification_type}"