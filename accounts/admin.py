from django.contrib import admin
from .models import CustomUser, Follow
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (id ,'username', 'email', 'first_name', 'last_name')

admin.site.register(Follow)

