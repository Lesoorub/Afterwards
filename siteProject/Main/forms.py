from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.models import User
from .models import Vote


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        exclude = ['start_user']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин...',
                'type': 'text',
                'id': 'login'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль...',
                'type': 'password',
                'id': 'password'
            })
        }


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ["title", "details"]
        widgets = {
            "title": TextInput(attrs={
                'type': 'text',
                'placeholder': 'Заголовок',
                'class': 'form-control'
            }),
            "details": Textarea(attrs={
                'type': 'text',
                'placeholder': 'Детали',
                'class': 'form-control'
            })
        }