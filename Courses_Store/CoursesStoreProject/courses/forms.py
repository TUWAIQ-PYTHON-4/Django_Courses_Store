from django import forms


class CourseForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    duration: forms.CharField()
    price = forms.IntegerField()
    image = forms.ImageField()
    online = forms.BooleanField()
    start_date = forms.DateTimeField()


class ReviewForm(forms.Form):
    rating = forms.IntegerField()
    comment = forms.CharField()


class UserForm(forms.Form):
    username = forms.CharField(label="Your username", max_length=64)
    email = forms.CharField(label="Your email", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)


class UserFormLogin(forms.Form):
    username = forms.CharField(label="Your username", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)
