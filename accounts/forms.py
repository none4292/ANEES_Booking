from django import forms
from . models import Proflie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Proflie
        fields = ['image','phone_number','address','gender']