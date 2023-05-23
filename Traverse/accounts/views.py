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

def myAccount(request):
    user_account = get_user_model().objects.get(pk=request.user.id)
    return render(request, 'traverse/myaccount.html', {'user_account':user_account})

def addAbout(request):
    if request.method == 'POST':
        form = AccountEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            new_edit = form.save(commit=False)
            new_edit.save()
        return HttpResponseRedirect(reverse('accounts:myaccount'))

    else:
        form = AccountEditForm()
    return render(request, 'traverse/edit_myaccount.html',  {'form':form})


def EditAbout(request):
    user = request.user
    if request.method == 'POST':
        form = AccountEditForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('accounts:myaccount'))
    else:
        form = AccountEditForm(instance = user)
    return render(request, 'traverse/edit_myaccount.html',  {'form':form, 'user':user})