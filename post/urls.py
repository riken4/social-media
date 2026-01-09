from django.urls import path
from . import views



urlpatterns = [
        path('', views.home_veiw, name='home'),
        path('create_post', views.create_post, name='create_post'),
        path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
        path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
        path('like_post/<int:post_id>', views.like_post, name='like_post'),
        path('add_comment/<int:post_id>', views.add_comment, name='add_comment'),
        path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
        path('/api/notification_api_view/<int:notification_id>', views.notification_api_view.as_view()),
        path('/api/mark_notification_read_api_view/<int:notification_id>', views.mark_notification_read_api_view.as_view()),
        path('/api/mark_all_notification_read_api_view/', views.mark_all_notification_read_api_view.as_view()),

]



#create admin pannel 
#admin insert data