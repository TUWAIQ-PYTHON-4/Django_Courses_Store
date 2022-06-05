from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission, Group
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import UserForm, UserFormLogin
from django.shortcuts import redirect, render, resolve_url
from .forms import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import login as auth_login


# Create your views here.

def home(request: HttpRequest):
    course = Course.objects.all()
    context={'course':course}
    return render(request, 'index.html', context)


def detail(request: HttpRequest ,course_id):
    if request.method == "POST":
        form = CourseForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = Course.objects.all()
            return render(request, 'detail.html', {'all_items': all_items})
    else:
        all_items = Course.objects.all()
        return render(request, 'detail.html', {'all_items': all_items})


def display_review(request: HttpRequest):
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = Review.objects.all()
            return render(request, 'detail.html', {'all_items': all_items})
    else:
        all_items = Review.objects.all()
        return render(request, 'detail.html', {'all_items': all_items})


@login_required(login_url="login")
def add_review(request: HttpRequest, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            added_review = Review(review=review, rating=review_form.cleaned_data["rating"],
                                  comment=review_form.cleaned_data["comment"], user=User)
            added_review.save()
        else:
            print(review_form.errors)
    context = {"review": review, "form": ReviewForm()}
    return render(request, 'detail.html', context)


def orders(request: HttpRequest,order_id):
    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = Order.objects.all()
            return render(request, 'orders.html', {'all_items': all_items})
    else:
        all_items =  Order.objects.all()
        return render(request, 'orders.html', {'all_items': all_items})


def register(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(user_form.cleaned_data["username"], user_form.cleaned_data["email"],
                                                user_form.cleaned_data["password"])
            new_user.save()

            return redirect(resolve_url('home'))

    return render(request, 'register.html', {'form': UserForm()})


def login(request:HttpRequest):
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


@login_required(login_url="login")
@permission_required("course.add_Course", login_url="login")
def add_Course(request: HttpRequest):
    if request.method == 'POST':
        courseForm = CourseForm(request.POST, request.FILES)

        if courseForm.is_valid():
            course = Course(user=request.user, **courseForm.cleaned_data)
            course.save()
            return redirect(resolve_url("home"))

    form = CourseForm()
    return render(request, 'add.html', {"form": form})


def add_course_permission(request: HttpRequest):
    if not request.user.has_perm("add_course"):
        contentType = ContentType.objects.get_for_model(Course)
        permission = Permission.objects.get(codename="add_course", content_type=contentType)
        request.user.user_permissions.add(permission)
    return HttpResponse("The permission is added")


def add_to_group_editors(request: HttpRequest):
    if not request.user.groups.filter(name="editors").exists():
        group = Group.objects.get(name="editors")
        request.user.groups.add(group)

    return HttpResponse("Added successfully ")