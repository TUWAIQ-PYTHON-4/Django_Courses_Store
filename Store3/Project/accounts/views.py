from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, resolve_url
from .forms import UserForm, UserFormLogin

from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login

from django.contrib.contenttypes.models import ContentType
import myproject.models as b


# Create your views here.


def register_user(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(user_form.cleaned_data["username"], user_form.cleaned_data["email"],
                                                user_form.cleaned_data["password"])
            new_user.save()

            return redirect('index')

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
                return redirect('index')
            else:
                return redirect('login')

    return render(request, 'login.html', {'form': UserFormLogin()})


def add_course_permission(requst: HttpRequest):
    if not requst.user.has_perm("myproject.add_course"):
        contentType = ContentType.objects.get_for_model(b.Post)
        permission = Permission.objects.get(codename="add_course", content_type=contentType)
        requst.user.user_permissions.add(permission)

    return HttpResponse("The permission is added")


def add_to_group_managers(request: HttpRequest):
    if not request.user.groups.filter(name="managers").exists():
        group = Group.objects.get(name="managers")
        request.user.groups.add(group)

    return HttpResponse("Added successfully in the Grouop!")

