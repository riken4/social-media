from django.urls import path
from . import views

urlpatterns = [
        path('/signup_view', views.signup_view, name='signup_view'),
        path('/login', views.login, name='login'),

        path('/logout', views.logout, name='logout'),
        # path('/profile/<str:username>', views., name=''),
        # path('/profile', views.profile, name='profile'),
        #name myprofile
        path('/follow_toogle/<str:username', views.follow_toggle, name='follow_toggle'),

]
