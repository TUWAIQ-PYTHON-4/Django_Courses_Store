from django.shortcuts import render,redirect, resolve_url, get_object_or_404
from .models import Course , Order
from .forms import reviewForm , CourseForm 
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.

def list_course(request):
    context={"course": Course.objects.all(),}
    return render (request,'index.html',context)

@permission_required("coursrsApp.add_course", login_url="login")
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect(resolve_url("home"))
        else:
            print(form.errors)
    form = CourseForm()
    return render(request, 'add-course.html', {"form" : form})

def comment_detile(request, pk):
    course=get_object_or_404(Course, pk=pk)
    if request.method=='POST':
       form= reviewForm(request.POST)

       if form.is_valid():
          obj= form.save(commit=False)
          obj.course=course
          obj.save()
          return redirect('course',pk=course.pk)
          
    form= reviewForm()
    context={'course':course,'form':form}
    return render(request,'course.html',context)

def buy(request, course_id):
    course = Course.objects.get(id=course_id)
    order = Order(user=request.user, course=course,totalprice=(course.price * 0.15)+course.price ,date=True)
    order.save()
    context = {'course':course}
    return render(request, 'order.html', context)

def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {'order':order}
    return render(request,'order.html',context)