from django import forms
from .models import Review, Course


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = "__all__"
        fields = ['comment', 'rating']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
