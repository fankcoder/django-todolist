from django.forms import ModelForm
from django import forms
from models import List
from django.contrib.auth.models import User

class CreateList(ModelForm):
    class Meta:
        model = List
        fields = ['title','content','level']

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
