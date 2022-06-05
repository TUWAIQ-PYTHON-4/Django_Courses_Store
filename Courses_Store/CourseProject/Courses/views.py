from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect

from CourseProject.Courses.form import OrderModelForm, ReviewModelForm, CourseModelForm
from CourseProject.Courses.models import courses, Order, Review


def index(request: HttpRequest):
    course = courses.objects.all()
    context = {'courses': course}
    response = render(request, 'index.html', context)
    return response

def add_course(request):
    if request.method == "POST":
        courseModelForm = CourseModelForm(request.POST, request.FILES)

        if courseModelForm.is_valid():
            course = courses(user=request.user, **courseModelForm.cleaned_data)
            course.save()
            return redirect('index')
    form = CourseModelForm()
    return render(request, 'add.html', {'form': form})

def base(request):
    return render(request, 'Courses/base.html')
def AddCourses(request):
    return render(request, 'Courses/AddCourses.html')
def home(request):
    return render(request, 'Courses/home.html')


def course_detail(request: HttpRequest, course_id):
    course = courses.objects.get(pk=course_id)

    if request.method == "POST":
        reviewModelForm = ReviewModelForm(request.POST)
        if reviewModelForm.is_valid():
            added_review = Review(user=request.user,  **reviewModelForm.cleaned_data)
            added_review.save()
        else:
            print(reviewModelForm.errors)

    context = {"course": course, "form": ReviewModelForm()}
    return render(request, 'detail.html', context)

@login_required
def buy(request, course_id):
    course = courses.objects.get(id=course_id)
    now = datetime.now()
    order = Order(user=request.user, courses=course,total_price=(course.price * 0.15)+course.price ,date=now)
    order.save()
    order= Order.objects.all()
    context = {'order':order, 'form' :OrderModelForm()}
    return render(request, 'Order.html', context)