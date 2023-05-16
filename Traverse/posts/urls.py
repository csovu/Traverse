from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.AllPosts, name="all"),
    path("account/", views.account, name="account"),
    path("profile/<int:user_id>/", views.Userprofile , name="profile"),
    path("create/", views.CreatePost, name="create"),
]