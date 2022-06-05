from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Review, Order, CartOrderItems
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from .cart import Cart
from .forms import ReviewForm, CourseForm
from django.contrib import messages


# Create your views here.


def all_courses(request: HttpRequest):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def course_detail(request: HttpRequest, id: int):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            added_comment = Review(
                comment=review_form.cleaned_data["comment"],
                rating=review_form.cleaned_data["rating"],
                course=course,
                customer=request.user
            )
            added_comment.save()
        else:
            print(review_form.errors)

    context = {'course': course, 'form': ReviewForm()}
    return render(request, 'course_details.html', context)


def cart_summary(request: HttpRequest):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})


def add_to_cart(request: HttpRequest):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        course_id = int(request.POST.get('courseid'))
        course = get_object_or_404(Course, id=course_id)
        cart.add(course=course)
        response = JsonResponse({'test': 'data'})
        return response


def search_course(request: HttpRequest):
    if request.method == 'POST':
        searched = request.POST['searched']
        course = Course.objects.filter(title__icontains=searched) | Course.objects.filter(
            description__icontains=searched)
        return render(request, 'search.html', {'searched': searched, 'course': course})
    else:
        return render(request, 'search.html', {})


def my_orders(request: HttpRequest):
    totalprice = 0
    if 'cartdata' in request.session:
        for id, item in request.session['cartdata'].items():
            totalprice += int(1.50) * float(item['price'])
        order = Order.objects.create(
            customer=request.user,
            totalprice=totalprice
        )
        for id, item in request.session['cartdata'].items():
            totalprice += 1.50 * float(item['price'])

            items = CartOrderItems(
                order=order,
                item=item['title'],
                image=item['image'],
                price=item['price'],
                total=1.50 * float(item['price'])
            )


def add_course(request):
    submitted = False
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_course?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_course.html', {'form': form, 'submitted': submitted})
