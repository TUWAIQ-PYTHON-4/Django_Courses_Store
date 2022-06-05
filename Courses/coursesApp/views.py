from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from .models import Course, Review, Order
from .forms import CourseForm, ReviewForm, OrderForm


# Create your views here.

def home(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


def course_detail(request, id):
    course_info = Course.objects.get(id=id)
    review_info = Review.objects.filter(course_id=course_info)
    context = {'course_info': course_info, 'review_info': review_info}
    return render(request, 'course_detail.html', context)


def add_course(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user.id
            course.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_course.html', {'form': form, 'submitted': submitted})


def add_review(request, id):
    submitted = False
    course_info = Course.objects.get(id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = Course.objects.get(id=id)
            review.user = request.user
            review.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = ReviewForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_review.html', {'form': form, 'submitted': submitted, 'course_info': course_info})


def order_course(request, id):
    course_info = Course.objects.get(id=id)
    order_info = Order.objects.filter(course_info=id)
    cart = Order(request)
    course = Course.objects.get(id=id)
    cart.add(course=course)
    return redirect("home")


def orders_detail(request, id):
    order = Order.objects.all()
    course_info = Course.objects.get(id=id)
    total = 0
    for i in order:
        total += (i.totale_price*0.15)
    order_info = Order.objects.create(date='2022-02-22', totale_price=course_info.price, course=course_info,
                                      user=request.user)
    order_info.save()
    context = {'course_info': course_info, 'order_info': order_info, 'order': order, 'total': total}
    return render(request, 'orders.html', context)


def show_detail(request):
    Order_info = Order.objects.filter(user=request.user)
    context = {'Order_info': Order_info}
    return render(request, 'orders.html', context)

