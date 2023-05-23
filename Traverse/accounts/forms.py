from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Button)
from django.urls import reverse_lazy
from accounts.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

# class createEditForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(createEditForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('save', "Save changes", css_class = 'btn-success'))
    
#     class Meta:
#         model = CustomUser
#         fields = ['location', 'about', 'profile_picture']


class AccountEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('save', "Save changes", css_class = 'btn-success'))
    
    class Meta:
        model = CustomUser
        fields = ['location', 'about', 'profile_picture']

