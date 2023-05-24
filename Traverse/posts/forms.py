from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Button)
from django.urls import reverse_lazy
from posts.models import *
from django.forms import inlineformset_factory

class CreatePostForm(forms.ModelForm):

    class Meta:
        model= Posts
        fields = ['trip_title', 'trip_summery', 'trail_conditions', 'planning_info', 'other_details','location', 'map_details']
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
        self.helper.add_input(Button('delete', 'Delete', onclick='window.location.href="{}"'.format('delete')))

    class Meta:
        model = Posts
        fields = ['trip_title', 'trip_summery', 'trail_conditions', 'planning_info', 'other_details','location', 'map_details']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']


ImageFormSet = inlineformset_factory(
    Posts,
    Image,
    fields = ['trip_title', 'trip_summery', 'trail_conditions', 'planning_info', 'other_details','location', 'map_details'],
    # form=ImageForm,
    min_num=1,
    extra=1,
    can_delete=False,

)