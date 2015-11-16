from django import forms
from django.contrib.auth.models import User

class Registration(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password", max_length=50)
    email = forms.EmailField(label="Email", max_length=255)

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=50)
