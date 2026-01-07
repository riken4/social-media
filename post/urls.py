from django.urls import path
from . import views



urlpatterns = [
        path('', views.home_veiw, name='home_view'),
        path('create_post', views.create_post, name='create_post'),
        path('edit_post/<int:post_id>', views.home, name='home'),
        path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]