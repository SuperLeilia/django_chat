from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

from .models import Profile


class UserRegisterForm(UserCreationForm):
    password1 = forms.RegexField(
        required=True,
        max_length=20,
        min_length=4,
        regex='^[1-9]*$',
        error_messages={
            'required': '请输入密码',
            'max_length': '密码长度不长于20位',
            'min_length': '密码长度不短于4位',
            'invalid': '密码格式不正确',
        },
        help_text='<ul>'
                  '<li>密码只能为数字</li>'
                  '<li>密码为4-20位</li>'
                  '</ul>',
        label='密码',
        widget=widgets.PasswordInput())

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []
