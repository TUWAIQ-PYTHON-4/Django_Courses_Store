from django import forms
from .models import *


class UserForm(forms.Form):
    username = forms.CharField(label="Your username", max_length=64)
    email = forms.CharField(label="Your email", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)


class UserFormLogin(forms.Form):
    username = forms.CharField(label="Your username", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)


class CourseForm(forms.Form):
    class Meta:
        model: Course
        fields = '__all__'


class ReviewForm(forms.Form):
    class Meta:
        model: Review
        fields = '__all__'
