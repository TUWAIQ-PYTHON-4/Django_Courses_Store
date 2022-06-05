from django import forms
from .models import *
from django.contrib.auth.forms import User # video youtube





class UserForm(forms.Form):
    username = forms.CharField(label="Your username", max_length=64)
    email = forms.CharField(label="Your email", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)


class UserFormLogin(forms.Form):
    username = forms.CharField(label="Your username", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)


class ReviewForm(forms.Form):
    rating = forms.IntegerField()
    comment = forms.Textarea()


class OrderForm(forms.Form):
    date = forms.DateTimeField()


class CourseForm(forms.Form):
    class Meta:
        model = Course
        fields = '__all__'
