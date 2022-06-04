
from django import forms
from .models import *

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class CourseOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
