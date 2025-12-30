from django.urls import path
from .views import get_posts, user_list

urlpatterns = [
    path("posts/", get_posts, name="get_posts"),
    path("users/", user_list, name="user_list"),
]