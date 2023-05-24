from django.urls import path 
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'

urlpatterns = [
    path("", views.AllPosts, name="all"),
    path("profile/<int:user_id>/", views.Userprofile , name="profile"),

    path("create/", views.PostImages, name="create"),
    path("post/<int:id>/", views.SinglePost, name="singlepost"),
    path("editpost/<int:id>/", views.EditPost, name="editpost"),
    path("editpost/<int:id>/delete", views.DeletePost, name="deletepost"),

    path("search/", views.SearchAll, name="search"),

    # path('upload/<int:id>/', views.PostImages, name='upload'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)