from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User


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
