from django import forms
from .models import Review , course
from django.forms import ModelForm
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')

class RegisterForm(forms.ModelForm):
    username = forms.CharField( max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(min_length=8)
    password2 = forms.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('error in password')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('username exit')
        return cd['username']

class courseform(ModelForm):
    class Meta:
        model = course
        fields = ('title','duration','start_date','price'
                  ,'online','user' , 'description','image')