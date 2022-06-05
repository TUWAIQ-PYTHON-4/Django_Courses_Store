from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Review, Order
from .forms import NewReview
from django.views.generic import CreateView


# Create your views here.
def home(request):
    search=Course.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search=search.filter(title__icontains=title)
    context = {
        #'course': Course.objects.all(),
        'course':search,
    }
    return render(request, 'courses/index.html', context)


def course_ditail(request, course_id):
    course = get_object_or_404(Course,pk=course_id)  # get_object_or_404 ( تنقلني من صفحه الى صفحه معينه وتاخذ بارميتر 2 بارميتر المودل والاي دي)
    commints = Review.objects.filter(course=course_id) #display all the review
    review_form=NewReview()
    new_review=None
    context = {
        'course': course,
        'commints': commints,
        'review_form':review_form,
    }

    # to add commant
    if request.method == 'POST':
        review_form = NewReview(data=request.POST)  # CommentForm name forms
        if review_form.is_valid():  # if the value corect--> save
            review_form = review_form.save(commit=False)
            review_form.course = course  # mapping with course
            review_form.save()
            review_form = NewReview()
    else:
        review_form = NewReview()

    # retern page
    return render(request, 'courses/ditail.html', context)

class CourseCreateView(CreateView):
    model=Course
    fields=['title','description','duration','price','image','online','start_date','user']
    template_name = 'courses/newcourse.html'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


def add_order(request, course_id):
    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=request.user.id)
    price_after_tax = course.price + (0.15 * course.price)
    new_order = Order.objects.create(order=course, totalprice=price_after_tax, user=user)
    return redirect("order")
def order1(request):
    orders = Order.objects.filter(user=request.user)
    total = Order.objects.aggregate(Sum('totalprice')).get("totalprice__sum")
    context = {"course": orders , "total":total}
    return render(request, 'courses/addorder.html', context)
