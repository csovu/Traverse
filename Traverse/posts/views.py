from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse, redirect
from posts.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import DetailView
from django.db.models import Q


def AllPosts(request):
    latest_post_list = Posts.objects.order_by("-pk")
    return render(request,'home.html', {'latest_post_list':latest_post_list})


def Userprofile(request, user_id):
    selected_user = get_user_model().objects.get(pk=user_id)
    user_posts = Posts.objects.filter(user = selected_user)
    return render(request,'traverse/profile.html', {'user_posts':user_posts, 'selected_user':selected_user})


def SinglePost(request, id):
    post = Posts.objects.get(pk=id)
    post_images = Image.objects.filter(posts_id = id)
    return render(request,'traverse/singlepost.html', {'post':post, 'post_images':post_images})


@login_required
def CreatePost(request):
    user = get_user_model().objects.get(pk=request.user.id)
    if request.method == 'GET':
        formset = ImageFormSet()
        createpost = CreatePostForm(request.GET or None)
        
    elif request.method == 'POST':
        formset = ImageFormSet(request.POST,request.FILES)
        createpost = CreatePostForm(request.POST)

        if createpost.is_valid() and formset.is_valid():
            post = createpost.save(commit=False)
            post.user = user
            post.save()

            images = formset.save(commit=False)
            for image in images:
                image.posts = post
                image.save()

            return HttpResponseRedirect(reverse('posts:all'))

    return render(request, 'traverse/create.html', {'formset':formset,'createpost':createpost})


@login_required
def EditPost(request, id):
    post = Posts.objects.get(pk=id)
    user = get_user_model().objects.get(pk=request.user.id)
    if request.method == 'GET':
        imagesform = ImageFormSet(queryset=Image.objects.none())
        postform = CreatePostForm(request.GET or None)
    if request.method == 'POST':
        postform = PostEditForm(request.POST, instance=post)
        imagesform = ImageFormSet(request.POST,request.FILES, instance=post)
        if postform.is_valid() and imagesform.is_valid():
            edit_post = postform.save(commit=False)
            edit_post.user = user
            edit_post.save()

            images = imagesform.save(commit=False)
            for image in images:
                image.posts = post
                image.save()
                  
        return redirect(reverse('posts:singlepost', args=[post.id]))

    else:
        postform = PostEditForm(instance=post)
    return render(request, 'traverse/editpost.html',  {'postform':postform, 'post':post, 'user':user, 'imagesform':imagesform})


@login_required
def DeletePost(request, id):
    user = get_user_model().objects.get(pk=request.user.id)
    post = Posts.objects.get(pk=id)
    if user == post.user:
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

@login_required
def DeleteImage(request, img_id, posts_id):
    post = Posts.objects.get(pk=posts_id)
    image = Image.objects.get(pk=img_id)
    image.delete()
    return redirect(reverse('posts:editpost', args=[post.id]))

