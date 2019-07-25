# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'email', 'country', 'jobs')
        widgets = {
            'email': forms.EmailInput(attrs={'required': 'true'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError('User {0} already exists'.format(username))
        return username

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Passwords don\'t match')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = MyUser
        fields = ('email', 'country', 'jobs')

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError('User {0} already exists'.format(username))
        return username

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Passwords don\'t match')
