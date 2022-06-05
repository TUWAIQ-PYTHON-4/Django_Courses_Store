from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerforms(UserCreationForm):
    email = forms.CharField(label="Your email", max_length=255,required=True,widget=forms.EmailInput())
    #username = forms.CharField( label="Your username", max_length=64)
    #password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)
    class Meta:
        model=User
        fields={'username','email'}

class UserFormLogin(forms.Form):

    username = forms.CharField( label="Your username", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)