from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.AllPosts, name="all"),
    path("myaccount/", views.myAccount, name="myaccount"),
    path("profile/<int:user_id>/", views.Userprofile , name="profile"),
    path("create/", views.CreatePost, name="create"),
    path("post/<int:id>/", views.SinglePost, name="singlepost"),
]