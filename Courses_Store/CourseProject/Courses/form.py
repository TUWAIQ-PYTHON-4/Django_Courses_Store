from django import forms
from .models import courses ,Review,Order



class CourseModelForm(forms.ModelForm):
    class Meta:
        model = courses
        fields = '__all__'
        exclude = ['user']

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user']


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'