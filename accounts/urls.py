from django.urls import path
from . import views

urlpatterns = [
        path('signup_view/', views.signup_view, name='signup'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('profile_view/<str:username>/', views.profile_view, name='profile_view'),
        path('follow_toggle/<str:username>/', views.follow_toggle, name='follow_toggle'),
]
