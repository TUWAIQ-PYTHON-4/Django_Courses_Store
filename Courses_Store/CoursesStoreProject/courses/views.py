from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
import courses.models as m
from django.contrib.contenttypes.models import ContentType
# Create your views here.
from .forms import CourseForm, ReviewForm, UserFormLogin, UserForm
from .models import Course, Review


def home(request: HttpRequest):
    home = Course.objects.all()
    context = {'index': home}
    return render(request, 'home.html', context)


def add_course(request: HttpRequest):
    if request.method == 'POST':
        courseForm = CourseForm(request.POST, request.FILES)

        if courseForm.is_valid():
            course = courseForm.save()
            return redirect(resolve_url('courses:home'))

    form = CourseForm()
    return render(request, 'add_course.html', {"form": form})


@login_required(login_url="login")
def course_detail(request: HttpRequest, course_id):
    course = Course.objects.get(pk=course_id)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            added_Review = Review(course=course, rating=review_form.cleaned_data["rating"],
                                  comment=review_form.cleaned_data["comment"])
            review_form.save()
        else:
            print(review_form.errors)

    context = {"course": course, "form": ReviewForm()}

    return render(request, 'course_detail.html', context)


def register_user(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
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


def add_course_permission(requst: HttpRequest):
    if not requst.user.has_perm("courses.add_course"):
        contentType = ContentType.objects.get_for_model(m.Course)
        permission = Permission.objects.get(codename="add_course", content_type=contentType)
        requst.user.user_permissions.add(permission)

    return HttpResponse("The permission is added")
