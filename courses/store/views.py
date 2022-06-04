from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import CourseModelForm, ReviewModelForm, OrderModelForm
from .models import Course, Review, Order
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.





def base(requset : HttpRequest):
    return render(requset, 'base.html')


def index(request : HttpRequest):
    course_list = Course.objects.all()

    context = {"course": course_list}
    response = render(request, 'index.html', context)
    return response



'''def add (request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CourseModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "add.html", context)
    '''
@login_required(login_url='/accounts/login')
@permission_required("store.add_course", login_url="/accounts/login")
def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST, request.FILES)

        if form.is_valid():
            course = Course(user=request.user, **form.cleaned_data)
            course.save()
            return redirect('index')
    form = CourseModelForm()
    return render(request, 'add.html', {'form': form})

@login_required(login_url='/accounts/login')

def detail(request: HttpRequest, course_id):
    course = Course.objects.get(pk=course_id)

    if request.method == "POST":
        reviewform = ReviewModelForm(request.POST)
        if reviewform.is_valid():
            added_review = Review(course=course, rate=ReviewModelForm.cleaned_data["rate"],
                                    comment=ReviewModelForm.cleaned_data["comment"])
            added_review.save()
        else:
            print(ReviewModelForm.errors)

    context = {"course": course, "form": ReviewModelForm()}
    return render(request, 'detail.html', context)

@login_required
def buy(request, course_id):
    course = Course.objects.get(id=course_id)
    now = datetime.now()
    order = Order(user=request.user, courses=course,total_price=(course.price * 0.15)+course.price ,date=now)
    order.save()
    order = Order.objects.all()
    context = {'order':order, 'form':OrderModelForm()}
    return render(request, 'order.html', context)