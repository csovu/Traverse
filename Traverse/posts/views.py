from django.shortcuts import render, reverse
from posts.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm


def AllPosts(request):
    latest_post_list = Posts.objects.order_by("-date_posted")[:10]
    return render(request,'home.html', {'latest_post_list':latest_post_list})


@login_required
def CreatePost(request):
    user = get_user_model().objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = user
            new_post.save()
        return HttpResponseRedirect(reverse('posts:all'))

    else:
         form = CreatePostForm()
    return render(request, 'traverse/create.html',  {'form':form, 'user':user})


def Userprofile(request, user_id):
    selected_user = get_user_model().objects.get(pk=user_id)
    user_posts = Posts.objects.filter(user = selected_user)
    return render(request,'traverse/profile.html', {'user_posts':user_posts, 'selected_user':selected_user})


def account(request, user_id):
    user_account = get_user_model().objects.get(pk=user_id)
    return render(request, user_account)