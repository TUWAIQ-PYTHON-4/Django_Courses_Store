from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Course, Review,Order
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CourseModelForm, ReviewModelForm, OrderModelForm

def index(request: HttpRequest):
    course = Course.objects.all()
    context = {'courses': course}
    response = render(request, 'index.html', context)
    return response

@login_required(login_url='/accounts/login')
@permission_required("myproject.add_course", login_url="/accounts/login")
def add_course(request):
    if request.method == "POST":
        courseModelForm = CourseModelForm(request.POST, request.FILES)

        if courseModelForm.is_valid():
            course = Course(user=request.user, **courseModelForm.cleaned_data)
            course.save()
            return redirect('index')
    form = CourseModelForm()
    return render(request, 'add.html', {'form': form})


def course_detail(request: HttpRequest, course_id):
    course = Course.objects.get(pk=course_id)

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
    course = Course.objects.get(id=course_id)
    now = datetime.now()
    order = Order(user=request.user, courses=course,total_price=(course.price * 0.15)+course.price ,date=now)
    order.save()
    order= Order.objects.all()
    context = {'order':order, 'form' :OrderModelForm()}
    return render(request, 'order.html', context)






