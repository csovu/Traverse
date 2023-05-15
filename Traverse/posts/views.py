from django.shortcuts import render
from posts.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm

def AllPosts(request):
    latest_post_list = Posts.objects.order_by("-date_posted")[:10]
    return render(request,'posts/home.html', {'latest_post_list':latest_post_list})


@login_required
def CreatePost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreatePostForm
    else:
        form = CreatePostForm()
    return render(request, 'traverse/create.html', {'form':form})


def profile(request, user_id):
    selected_user = get_user_model().objects.get(pk=user_id)
    all_posts = Posts.objects.filter(user = selected_user)
    return render(request,'traverse/profile.html', {'all_posts':all_posts})