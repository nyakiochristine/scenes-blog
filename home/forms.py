from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields=('captions','image')