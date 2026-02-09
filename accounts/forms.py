from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"johndoe123"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder":"johndoe123@gmail.com"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"*************"
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"*************"
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']