from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Button)
from django.urls import reverse_lazy
from posts.models import *
from django.forms import inlineformset_factory
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

class CreatePostForm(forms.ModelForm):

    class Meta:
        model= Posts
        fields = ['trip_title','location', 'trip_summery', 'planning_info', 'other_details', 'map_details']
        widgets ={
              'trip_title': forms.TextInput(attrs={
                'style': 'min-width: 400px;',
        }),
        'trip_summery': forms.TextInput(attrs={
                'style': 'min-width: 400px;'
                'min-height: 100px',
        }),
        'planning_info': forms.TextInput(attrs={
                'style': 'min-width: 400px;'
                'min-height: 100px',
        }),
        'other_details': forms.TextInput(attrs={
            'placeholder': 'any other plannning or trip considerations',
            'style': 'min-width: 400px;'
            'min-height: 100px',
        }),
        'map_details': forms.TextInput(attrs={
            'placeholder': 'Map Link',
        }),
        }
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
        fields = ['trip_title','location', 'trip_summery', 'planning_info', 'other_details', 'map_details']
        widgets ={
              'trip_title': forms.TextInput(attrs={
                'style': 'min-width: 400px;',
        }),
        'trip_summery': forms.TextInput(attrs={
                'style': 'min-width: 400px;'
                'min-height: 100px',
        }),
        'planning_info': forms.TextInput(attrs={
                'style': 'min-width: 400px;'
                'min-height: 100px',
        }),
        'other_details': forms.TextInput(attrs={
            'placeholder': 'any other plannning or trip considerations',
            'style': 'min-width: 400px;'
            'min-height: 100px',
        }),
        'map_details': forms.TextInput(attrs={
            'placeholder': 'Map Link',
        }),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','image']
        widgets ={
            'title': forms.TextInput(attrs={
            'placeholder': 'image title'
        })
        }

ImageFormSet = inlineformset_factory(
    Posts,
    Image,
    form=ImageForm,
    min_num=1,
    extra=0,
    can_delete=False,

)