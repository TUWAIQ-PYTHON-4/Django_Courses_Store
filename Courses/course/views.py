from django.shortcuts import render, redirect, resolve_url
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    all_courses= Course.objects.all()

    return render(request, 'course/home.html', {'courses': all_courses })


#@login_required(login_url="/accounts/login")

def add_course(request):

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)

        if course_form.is_valid():
           course = course_form.save()
           return redirect('home')


    form = CourseForm()
    return render(request, 'course/add_course.html', {"form": form})


def course_detail(request, course_id):

    course_info = Course.objects.get(pk=course_id)

    if request.method == "POST":
        rev_form = ReviewForm(request.POST)
        if rev_form.is_valid():
            rev_form.save()
        else:
            print(rev_form.errors)

    course_review = Review.objects.filter(course=course_id)

    return render(request, 'course/course_detail.html', {'course': course_info, "form": ReviewForm(), "reviews": course_review})

def course_orders(request,course_id):

    course_orders = Course.objects.get(pk=course_id)


    course_order = CourseOrderForm(request.POST)
    if course_order.is_valid():
        added_order = Order(course=course_orders, user=User.objects.get(id=request.user.id) ,total_price=(course_order.totalprice * 0.15))
        course_order.save()
    else:
        print(course_order.errors)

    orders = Order.objects.all()

    return render(request, 'course/course_orders.html', {'course_orders': orders, 'form': CourseOrderForm})
