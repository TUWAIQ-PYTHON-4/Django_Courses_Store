

from django.db.models import Sum

from django.shortcuts import render,redirect,resolve_url
from . models import *
from .forms import *
from django.db.models import Q


# Create your views here.


def home(request):
    courses= Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home.html', context)

def search(request):
    search_course = request.GET.get("search")
    if search_course:
        courses = Course.objects.filter(Q(title__icontains=search_course) & Q(description__icontains=search_course))
    else:

        courses = Course.objects.all().order_by("-date_created")
    return render(request, 'search.html', {"courses":courses})

def course_details(request , course_id):
    course = Course.objects.get(pk=course_id)
    user = User.objects.get(id = request.user.id)
    reviews = Review.objects.filter(course=course_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            add_Review = Review(course=course, rating=review_form.cleaned_data["rating"], comment=review_form.cleaned_data["comment"],user=user)
            add_Review.save()
        else:
            print(review_form.errors)
    context = {"course": course, "form": ReviewForm(), "reviews":reviews}
    return render(request, 'details.html', context)

def add_order(request, course_id):
    course = Course.objects.get(id=course_id)  # assuming that there is no user and the course_id is always valid existing course id
    user = User.objects.get(id=request.user.id)  # this must always be request.user assuming user is logged in
    price_after_tax = course.price + (0.15 * course.price)
    new_order = Order.objects.create(order=course, totalprice=price_after_tax, user=user)  # assuming the same
    return redirect("order")
def order1(request):
    orders = Order.objects.all() #when you login make this work with logged in user
                                #order.objects.filter(user=request.user) but also make sure user is authenticated
    total = Order.objects.aggregate(Sum('totalprice')).get("totalprice__sum")
    context = {"course": orders , "total":total}
    return render(request, 'AddOrder.html', context)

def add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(resolve_url("home"))
        print(form.errors)
    form = CourseForm()
    return render(request, 'add.html', {"form": form})


from django.contrib.auth import authenticate, login
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = authenticate(request, username=username, password=password,email=email)
    if user is not None:
        login(request, user)
# Redirect to a success page.
    else:
       return render(request, 'register.html')

def dashboard(request):
    return render(request, "dashboard.html")

def user_register(request):
    template = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'register.html', {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.save()
                login(request, user)
                return render(request,'admin')
    else:
        form = RegisterForm()
        return render(request, template, {'form': form})
    return redirect(resolve_url("/dashboard"))


