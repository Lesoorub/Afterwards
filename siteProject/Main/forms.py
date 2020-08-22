from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.models import User
from .models import Vote


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
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
        fields = ["title", "details", "start_time"]
        widgets = {
            "title": TextInput(attrs={}),
            "details": Textarea(attrs={})
        }