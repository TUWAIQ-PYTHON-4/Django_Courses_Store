from django import forms
from .models import Course, Review, Order
from django.forms import ModelForm


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        exclude = ['user']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ['user', 'course']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ['user','course','totale_price','date']
