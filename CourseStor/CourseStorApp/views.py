from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, resolve_url
from .forms import *
from .models import *


# Create your views here.
def home(request: HttpRequest):
    courses = Course.objects.all()

    context = {"courses": courses}
    return render(request, 'home.html', context)


# , course_id
# pk=course_id
def detail(request: HttpRequest, course_id):
    course = Course.objects.get(pk=course_id)
    # return render(request, 'detail.html', {})

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():

            added_comment = Review(course=course, name=review_form.cleaned_data["name"],
                                   content=review_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(review_form.errors)
    context = {"course": course}

    return render(request, 'detail.html', context, ReviewForm)


def login(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserFormLogin(request.POST)

        if user_form.is_valid():
            if not request.user.has_perm("course.add_course"):
                return redirect(resolve_url("accounts:login"))

            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            authenticate_user = authenticate(request, username=username, password=password)

            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect(resolve_url('home'))
            else:
                return redirect(resolve_url('login'))

    return render(request, 'login.html', {'form': UserFormLogin()})


def order(request: HttpRequest, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'orders.html', course)


def register(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(user_form.cleaned_data["username"], user_form.cleaned_data["email"],
                                                user_form.cleaned_data["password"])
            new_user.save()

            return redirect(resolve_url('home'))

    return render(request, 'register.html', {'form': UserForm()})


@login_required(login_url="login")
@permission_required("course.add", login_url="login")
def add(request: HttpRequest):
    if request.method == 'POST':
        courseForm = CourseForm(request.POST, request.FILES)

        if courseForm.is_valid():
            course = Course(user=request.user, **courseForm.cleaned_data)
            course.save()
            form = {'course': course}
            return redirect(resolve_url("home"), form)

    form = CourseForm()
    return render(request, 'add.html', {"form": form})


def checkout(request: HttpRequest):
    return render(request, 'checkout.html')
