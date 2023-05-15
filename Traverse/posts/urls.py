from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path("home", views.AllPosts, name="home"),
    path("profile/<int:user_name_id>", views.profile , name="profile"),
    path("create/", views.CreatePost, name="create"),
]