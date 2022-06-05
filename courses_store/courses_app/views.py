from django.shortcuts import render, redirect, resolve_url
from .models import *
from .forms import *



def index(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'index.html', context)

def course_detail(request, course_id ):

    current_user = request.user.username
    courses_reviews = Reviews.objects.filter(course_id = course_id)
    course_info = Courses.objects.get(pk = course_id)

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            Review = Reviews.objects.create(course_id=course_id,user = request.user,
                             rating = request.POST['rating'], comment = request.POST['comment'])
            return redirect(resolve_url("course_detail",course_id))
    else:
        form = ReviewsForm()


    context = {'course_info': course_info,
               'current_user': current_user,
               'courses_reviews': courses_reviews,
               'form': form}
    return render(request, 'course_detail.html', context)

def course_form(request):
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            courses = Courses.objects.create(user = request.user, title = request.POST['title'].title(),
            description = request.POST['description'], duration = request.POST['duration'],
            price = request.POST['price'],online = request.POST['online'],
            start_date = request.POST['start_date'], image = request.FILES['image'])
            return redirect(resolve_url("index"))
    else:
        form = CoursesForm()

    context = {'form': form}
    return render(request, 'course_form.html', context)

def Orders(request,course_id ):
    request.session["Orders"] = request.session.get("Orders",[]) + [course_id]
    print(request.session.get("Orders"))

    return redirect(resolve_url("course_detail", course_id))

def display_orders(request):
 try:
    list_of_orders = {Courses.objects.get(pk=i).title: calc_tax(Courses.objects.get(pk=i).price)
                      for i in request.session.get("Orders")}
    total_price = sum(list_of_orders.values())

    context = {'list_of_orders':list_of_orders, 'total_price': total_price}
    return render(request, 'orders.html', context)
 except:
     print('empty basket')
     return redirect(resolve_url("index"))



def checkout(request):
    if request.user.is_authenticated:
        del request.session['Orders']
        return redirect(resolve_url("index"))

    else:
        print('login or register to checkout')
        return redirect(resolve_url("login"))



def calc_tax(price)->int:
    c = int(price)
    return c+c*0.15