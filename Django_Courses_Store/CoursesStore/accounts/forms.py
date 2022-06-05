from django import forms

class UserForm(forms.Form):

    username = forms.CharField( label="Your username", max_length=64)
    email = forms.CharField(label="Your email", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)
    first_name = forms.CharField(label="Your first name", max_length=64)
    last_name = forms.CharField(label="Your last name", max_length=64)


class UserFormLogin(forms.Form):

    username = forms.CharField( label="Your username", max_length=64)
    password = forms.CharField(label="Your password", widget=forms.widgets.PasswordInput)
