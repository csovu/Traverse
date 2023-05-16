from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.AllPosts, name="all"),
    path("account/", views.account, name="account"),
    path("profile/<int:user_id>/", views.profile , name="profile"),
    path("create/", views.CreatePost, name="create"),
    # path("create/save", views.CreatePost, name="save"),
]