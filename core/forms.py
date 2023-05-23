from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full p-2 rounded-md text-sm'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'name@email.com',
        'class': 'w-full p-2 rounded-md text-sm'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 rounded-md text-sm'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 rounded-md text-sm'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full p-2 rounded-md text-sm'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 rounded-md text-sm'
    }))
