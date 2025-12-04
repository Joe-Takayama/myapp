from django.forms import ModelForm, TextInput, PasswordInput
from .models import User
from django import forms


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': '名前を入力してください。'
            }),
            'password': PasswordInput(attrs={
                'placeholder': 'パスワードを入力してください。'
            }),
        }

class LoginForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='名前',
        widget=forms.TextInput(attrs={
            'placeholder': '名前を入力してください。'
        })
    )
    password = forms.CharField(
        max_length=255,
        label='パスワード',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'パスワードを入力してください。'
        })
    )