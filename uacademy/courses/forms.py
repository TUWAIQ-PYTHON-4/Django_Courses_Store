from django import forms
from .models import Course, Review
from django.contrib.auth.models import User


class CourseForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField()
    duration = forms.IntegerField()
    price = forms.DecimalField(decimal_places=2, max_digits=6)
    image = forms.ImageField()
    online = forms.BooleanField()
    start_date = forms.DateTimeField()

class CourseModelForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__' #to include all fields
        exclude = ['user']


class ReviewForm(forms.Form):
    rate = forms.ChoiceField(choices=[["1", "1 Star"], ["2", "2 Stars"]], widget=forms.widgets.RadioSelect)
    comment = forms.CharField()
    # user = forms.ForeignKey(User)


    