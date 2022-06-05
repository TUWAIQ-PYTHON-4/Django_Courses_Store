from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'description', 'start_date', 'duration', 'online', 'price', 'image']
        widgets = {'start_date': DateInput(), }

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['rating', 'comment']