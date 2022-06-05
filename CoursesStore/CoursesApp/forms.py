from django import forms
from .models import Review
class NewReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment','rating','user')

