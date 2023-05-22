from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

def EditAbout(request):

    if request.method == 'POST':
        form = AccountEditForm(request.POST, instance=request.user)
        if form.is_valid():

            form.save()
        return HttpResponseRedirect(reverse('posts:myaccount'))

    else:
        form = AccountEditForm()
    return render(request, 'traverse/edit_myaccount.html',  {'form':form})