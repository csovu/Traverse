from django.shortcuts import render
from posts.models import *
from django.contrib.auth import get_user_model



# def AllPosts(request):
#     latest_post_list = Posts.objects.order_by("-pub_date")[:10]
#     return render(request,'posts/home.html', {'latest_post_list':latest_post_list})



# def profile(request, user_name_id):
#     selected_user = get_user_model().objects.get(pk=user_name_id)
#     all_posts = Posts.objects.filter(user_name = selected_user)
#     return render(request,'posts/profile.html', {'all_posts':all_posts})