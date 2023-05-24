from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse, redirect, get_object_or_404
from posts.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import DetailView
from django.db.models import Q
from django.forms import modelformset_factory

def AllPosts(request):
    latest_post_list = Posts.objects.order_by("-date_posted")[:10]
    return render(request,'home.html', {'latest_post_list':latest_post_list})


def Userprofile(request, user_id):
    selected_user = get_user_model().objects.get(pk=user_id)
    user_posts = Posts.objects.filter(user = selected_user)
    return render(request,'traverse/profile.html', {'user_posts':user_posts, 'selected_user':selected_user})



def SinglePost(request, id):
    onepost = Posts.objects.filter(id=id)
    return render(request,'traverse/singlepost.html', {'onepost':onepost})


@login_required
# def CreatePost(request):
#     user = get_user_model().objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         form = CreatePostForm(request.POST)
#         if form.is_valid():
#             new_post = form.save(commit=False)
#             new_post.user = user
#             new_post.save()
#         return HttpResponseRedirect(reverse('posts:all'))

#     else:
#         form = CreatePostForm()
#     return render(request, 'traverse/create.html',  {'form':form, 'user':user})


def PostImages(request):
    user = get_user_model().objects.get(pk=request.user.id)
    # post = Posts.objects.get(pk=id)
    formset = ImageFormSet(request.POST or None, request.FILES)

    if request.method == 'POST':

        if formset.is_valid():
            formset.instance = user
            formset.save()
            return HttpResponseRedirect(reverse('posts:all'))

    return render(request, 'traverse/create.html', {"formset":formset,'user':user})


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
    user = get_user_model().objects.get(pk=request.user.id)
    if user == post.user:
        post = get_object_or_404(Posts, pk=id)
        post.delete()
    else:
        return render(request,'home.html')
    return HttpResponseRedirect(reverse('posts:all'))


def SearchAll(request):
    query = request.GET.get("q")
    users = get_user_model().objects.filter(username__contains=query)
    print(users)
    object_list = Posts.objects.filter(
        Q(trip_title__contains=query) | Q(trip_summery__contains=query)
    ) 
    return render(request, 'traverse/search_results.html',  {'object_list':object_list, 'users':users})

