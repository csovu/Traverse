from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path("myaccount/", views.myAccount, name="myaccount"),
    path("addabout/", views.addAbout, name="addabout"),
    path("editabout/", views.EditAbout, name="editabout"),
]