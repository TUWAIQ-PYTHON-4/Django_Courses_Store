from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from .forms import UserRegisterForm, UserLoginForm, CourseModelForm, ReviewModelForm
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from .models import Course, Review


# works good
def Home(request):
    courses = Course.objects.all()
    return render(request, "home.html", {'courses': courses})


def Course_Detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    reviews = Review.objects.filter(course=course_id)
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        review_form = ReviewModelForm(request.POST)
        if review_form.is_valid():
            new_review = Review(course=course, rating=review_form.cleaned_data["rating"],
                                comment=review_form.cleaned_data["comment"], user=user)
            new_review.save()
        else:
            print(review_form.errors)

    return render(request, "course-detail.html", {"course": course, "form": ReviewModelForm(), "reviews": reviews})


def Orders(request):
    return render(request, "orders.html")


# works good
def Register(request: HttpRequest):
    if request.method == "POST":
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            new_account = User.objects.create_user(reg_form.cleaned_data["username"],
                                                   reg_form.cleaned_data["email"],
                                                   reg_form.cleaned_data["password"])
            new_account.save()
            return redirect(resolve_url('Store:Home'))
    return render(request, "register.html", {'form': UserRegisterForm()})


# works good
def Login(request: HttpRequest):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect(resolve_url('Store:Home'))
            else:
                return redirect(resolve_url('Store:Login'))
    return render(request, "login.html", {'form': UserLoginForm()})


# check thr functionality
def Add_Permission(request: HttpRequest):
    if not request.user.has_perm("courses.add_course"):
        contentType = ContentType.objects.get_for_model(Course)
        permission = Permission.objects.get(codename="add_course", content_type=contentType)
        request.user.user_permissions.add(permission)
    return HttpResponse("Now you have the permission of adding courses.")


# check thr functionality
@login_required(login_url="Store:Login")
@permission_required("courses.add_course", login_url="Store:Login")
def Add_Course(request: HttpRequest):
    if not request.user.has_perm("courses.add_course"):
        return redirect(resolve_url('Store:Login'))
    if request.method == "POST":
        form = CourseModelForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course(user=request.user, **form.cleaned_data)
            course.save()
            return redirect(resolve_url('Store:Home'))
        else:
            print(form.errors)
    item = CourseModelForm()
    return render(request, "add-course.html", {'item': item})
