import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Course,Review,Order
from .forms import CourseModelForm,ReviewModelForm,OrderModelForm

def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    response = render(request,'index.html',context)
    return response

@login_required(login_url='accounts/login')
def details(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        review_form = ReviewModelForm(request.POST,request.FILES)
        if review_form.is_valid():
            review = Review(user = request.user,course=course, **review_form.cleaned_data)
            review.save()
        else:
            print(review_form.errors)
    context = {'course':course, 'form':ReviewModelForm()}
    return render(request, 'details.html', context)

@login_required
def buy(request, course_id):
    course = Course.objects.get(id=course_id)
    now = datetime.datetime.now()
    order = Order(user=request.user, course=course,totalprice=(course.price * 0.15)+course.price ,date=now)
    order.save()
    context = {'course':course, 'form':OrderModelForm()}
    return render(request, 'orders.html', context)

def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {'order':order}
    return render(request,'orders.html',context)


@permission_required("coursesapp.add_course", login_url="accounts/login")
def add_course(request):
    now = datetime.datetime.now()
    if request.method == "POST":
        courseModel = CourseModelForm(request.POST, request.FILES)
        if courseModel.is_valid():
            course = CourseModelForm(user=request.user, start_date=now, **courseModel.cleaned_data)
            course.save()
            return redirect('index')
    form = CourseModelForm()
    return render(request, 'add_course.html', {'form':form})