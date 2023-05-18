from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Layout, ButtonHolder)
from django.urls import reverse_lazy
from posts.models import *


# class CreatePostForm(ModelForm):
#     class Meta:
#         model = Posts
#         fields = '__all__'

class CreatePostForm(forms.ModelForm):
    # trip_title = forms.CharField(max_length=50) 
    # trip_summery = forms.CharField(max_length=2000, widget=forms.Textarea())
    # trail_conditions = forms.CharField(max_length=2000, widget=forms.Textarea())
    # planning_info = forms.CharField(max_length=2000, widget=forms.Textarea())
    # other_details = forms.CharField(max_length=2000, widget=forms.Textarea())
    # location= forms.CharField(max_length=100)
    # map_details = forms.URLField(max_length=300) 
    class Meta:
        model= Posts
        fields = ['trip_title', 'trip_summery', 'trail_conditions', 'planning_info', 'other_details','location', 'map_details']
        # exclude = ['user']
    def __init__(self, *args, **kwargs):
    
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id='id-exampleFrom'
        self.helper.form_class='blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action= reverse_lazy('posts:create')
        self.helper.add_input(Submit('submit', 'Submit', css_class = 'btn-success')) 


class PostEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('save', "Save changes", css_class = 'btn-success'))

    class Meta:
        model = Posts
        fields = ['trip_title', 'trip_summery', 'trail_conditions', 'planning_info', 'other_details','location', 'map_details']

