from django.urls import path 
from . import views
from .views import SearchAll
app_name = 'posts'

urlpatterns = [
    path("", views.AllPosts, name="all"),
    path("profile/<int:user_id>/", views.Userprofile , name="profile"),
    path("create/", views.CreatePost, name="create"),
    path("post/<int:id>/", views.SinglePost, name="singlepost"),
    path("editpost/<int:id>/", views.EditPost, name="editpost"),
    path("editpost/<int:id>/delete", views.DeletePost, name="deletepost"),
    path("search/", views.SearchAll, name="search"),
    # path('upload/', views.image_upload)
]