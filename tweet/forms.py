from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = [
            'text',
            'photo',
        ]

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')