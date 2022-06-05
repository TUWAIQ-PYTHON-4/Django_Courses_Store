from django import forms
from .models import Course, Review, Order


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=30)
    email = forms.EmailField(label="email", max_length=50)
    password = forms.CharField(label="password", widget=forms.widgets.PasswordInput)


class UserLoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=30)
    # email = forms.EmailField(label="email", max_length=50)
    password = forms.CharField(label="password", widget=forms.widgets.PasswordInput)


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['user']


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class OrderModelForm(forms.ModelForm):
    model = Order

    class Meta:
        fields = '__all__'
