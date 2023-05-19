from django.shortcuts import render, reverse, get_object_or_404
from posts.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *


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


def myAccount(request):
    user_account = get_user_model().objects.get(pk=request.user.id)
    return render(request, 'traverse/myaccount.html', {'user_account':user_account})

def SinglePost(request, id):
    onepost = Posts.objects.filter(id=id)
    return render(request,'traverse/singlepost.html', {'onepost':onepost})

@login_required
def EditPost(request, id):
    post = Posts.objects.get(pk=id)
    user = get_user_model().objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.user = user
            edit_post.save()
        return HttpResponseRedirect(reverse('posts:all'))

    else:
        form = PostEditForm(instance=post)
    return render(request, 'traverse/editpost.html',  {'form':form, 'post':post, 'user':user})

@login_required
def DeletePost(request, id):
    # if request.user.id == post.user.id:
        post = get_object_or_404(Posts, pk=id)
        post.delete()
    # else:
    #     return render(request,'home.html')
        return HttpResponseRedirect(reverse('posts:all'))

