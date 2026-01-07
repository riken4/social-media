from django.contrib import admin
from .models import CustomUser,Post, Like, Comment, Notification
# Register your models here.


admin.site.register(CustomUser) 
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'profile_picture', 'location', 'created_at', 'updated_at')

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Notification)