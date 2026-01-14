from django.urls import path
from accounts.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
