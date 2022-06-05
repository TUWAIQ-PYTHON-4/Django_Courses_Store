from django import forms
from .models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = 'rating', 'content'
