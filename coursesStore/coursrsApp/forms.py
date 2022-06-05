from .models import Review, Course
from django.forms import ModelForm


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
class reviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('rating','comment','user')

