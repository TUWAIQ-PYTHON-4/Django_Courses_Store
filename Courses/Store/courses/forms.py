from django import forms
from .models import Cuorse , Order


class coursesform(forms.ModelForm):
    class Meta :
        model = Cuorse
        fields = '__all__'
        exclude = ['user']


class commentForm(forms.Form):
    rating = forms.CharField(max_length=10)
    comment = forms.CharField(widget=forms.widgets.Textarea)



class ordermodelform(forms.ModelForm):
    class meta :
        model = Order
        exclude = '__all__'
