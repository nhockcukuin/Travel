from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Posts

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
    
        # widgets = {
        #         'category':forms.CheckboxSelectMultiple(),
        #     }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']