from django.http import HttpRequest
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required, permission_required
from .models import Review, Course
from .forms import *


# Create your views here.
def home(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'CoursesStoreApp/home.html', context)


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/CoursesStore/')
        print(form.errors)
    form = CourseForm()
    return render(request, 'CoursesStoreApp/add_course.html', {"form": form})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = Review(user=request.user, course=course)
            review.save()
        else:
            print(review_form.errors)
    context = {'course': course, 'form': ReviewForm()}
    return render(request, 'CoursesStoreApp/detail.html', context)



