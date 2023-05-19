from django.urls import include, path
from .views import *
from . import views

appname = 'apis'

urlpatterns = [
    path('editabout/', AboutView.as_view()),

]