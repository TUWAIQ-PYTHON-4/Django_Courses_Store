from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, resolve_url
from .forms import UserForm, UserFormLogin

from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
import courses.models as c


def register_user(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # to regiser a new user
            new_user = User.objects.create_user(user_form.cleaned_data["username"], user_form.cleaned_data["email"],
                                                user_form.cleaned_data["password"])
            new_user.save()

            return redirect(resolve_url('home'))

    return render(request, 'register.html', {'form': UserForm()})


def login_user(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserFormLogin(request.POST)

        if user_form.is_valid():

            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            authenticate_user = authenticate(request, username=username, password=password)

            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect(resolve_url('home'))
            else:
                return redirect(resolve_url('login'))

    return render(request, 'login.html', {'form': UserFormLogin()})

