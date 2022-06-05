from django.db.models import Sum
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
    course_review = Review.objects.filter(course=course_id)
    print(course_review)
    if request.method == "POST":
        rev_form = ReviewForm(request.POST)
        if rev_form.is_valid():
            rev_form.save()
        else:
            print(rev_form.errors)
    return render(request, 'course/course_detail.html', {'course': course_info, "form": ReviewForm(), "reviews": course_review})


'''def course_orders(request,course_id):
    orders = Order.objects.all()
    ordered_course_info = Course.objects.get(pk=course_id)

    order_total =0
    for total in orders:
        order_total +=(total.totalprice * 0.15)
        print(total.totalprice)

    added_order = Order.objects.create(course=ordered_course_info, user=request.user, totalprice=ordered_course_info.price)
    added_order.save()

    return render(request, 'course/course_orders.html', {'course_orders_info': ordered_course_info, 'orders': orders, 'total': order_total })
'''

def course_orders(request,course_id):
    ordered_course = Course.objects.get(pk=course_id)
    user = User.objects.get(id=request.user.id)
    price_after_tax= ordered_course.price + (0.15 *ordered_course.price )
    added_order = Order.objects.create(course=ordered_course, user=user,totalprice=price_after_tax)
    orders = Order.objects.filter(user=user)
    total = Order.objects.aggregate(Sum('totalprice')).get('totalprice__sum')

    return render(request, 'course/course_orders.html', {'course': orders, 'total':total })
