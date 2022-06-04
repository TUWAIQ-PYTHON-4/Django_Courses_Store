from django import forms
from .models import Course,Review,Order

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['user','start_date']


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user','course']
    
class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = '__all__'