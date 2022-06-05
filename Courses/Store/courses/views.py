import datetime
from django.shortcuts import render , redirect , resolve_url
from .models import Cuorse , Review , Order
from .forms import commentForm , coursesform , ordermodelform
from django.contrib.auth.decorators import login_required , permission_required
# Create your views here.


def home(request):
    all_course =Cuorse.objects.all()
    context = {'all_course' : all_course}

    return render(request, 'home.html' , context)

@login_required(login_url="/accounts/login")
def details(request , course_id):
    course = Cuorse.objects.get(pk=course_id)
    if request.method == "POST":
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Review(course=course,user=request.user, rating=comment_form.cleaned_data["rating"],
                                    comment=comment_form.cleaned_data["comment"])
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {"course": course , "form": commentForm()}

    return render(request, 'details.html' , context)

@login_required(login_url="/accounts/login")
@permission_required("store.add_cuorse", login_url="/accounts/login")
def add(request):
    if request.method == 'POST':
        form = coursesform(request.POST , request.FILES)

        if form.is_valid():
            add_user = Cuorse(user=request.user, **form.cleaned_data)
            add_user.save()
            return redirect('home')

    form = coursesform()
    return render(request, 'add.html', {"form": form})

def buy (request , course_id):
    course = Cuorse.objects.get(pk=course_id)
    n = datetime.datetime.now()
    order = Order(user = request.user , course= course , totalprice=(course.price*0.15) + course.price,date=n)
    order.save()
    order=Order.objects.filter(user_id= request.user)
    context = {'order' : order }
    return render(request,'order.html', context)

@login_required(login_url="/accounts/login")
def getMyOrders (request):
    order=Order.objects.filter(user_id = request.user)
    context = {'order' : order }
    return render(request,'order.html', context)


