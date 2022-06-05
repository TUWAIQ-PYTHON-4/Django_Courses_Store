from multiprocessing import context
from socket import IP_DROP_MEMBERSHIP
from tokenize import maybe
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Course, Review, Order
from django.core.paginator import Paginator
from .forms import CourseForm, CourseModelForm, ReviewForm
# Create your views here.

def courses(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'courses': courses,
        'page_obj': page_obj,
    }
    return render(request, 'courses/home.html', context)


def course_details(request:HttpRequest, course_id):
    course = Course.objects.get(pk=course_id)

    if request == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            add_review = Review(course=course, rate=review_form.cleaned_data['rate'], comment=review_form.cleaned_data['comment'], user=review_form.cleaned_data['user'])
            add_review.save()

    context = {'couse': course, 
               'form': ReviewForm}
    return render(request, 'courses/course_detail.html', context)


@login_required(login_url="/users/login")
def orders(request : HttpRequest):

    if 'my_courses' in request.GET:
       my_courses = request.session.get('order', [])
       orders = Order.objects.filter(id__in=my_courses)
    
    else: 
        orders = Order.objects.all()

    paginator = Paginator(courses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'orders': orders,
        'page_obj': page_obj,
    }
    return render(request, 'courses/orders.html', context)


@login_required(login_url="/users/login")
def add_course(request : HttpRequest):

    # Check for permission
    if not request.user.has_perm("courses.add_course"):
        return redirect(resolve_url("users:login"))

    if request.method == 'POST':
        courseModelForm = CourseModelForm(request.POST, request.FILES)

        if courseModelForm.is_valid():
            # add model
            course = Course(user=request.user,  **courseModelForm.cleaned_data)
            course.save()
            return redirect(resolve_url("course:courses")) 

    form = CourseModelForm()
    return render(request, 'courses/add_course.html', {"form" : form})


@login_required(login_url="/users/login")
def add_order(request:HttpRequest, order_id):
    
    request.session["order"] = request.session.get("order", []) + [order_id]
    return redirect(resolve_url("courses:courses"))