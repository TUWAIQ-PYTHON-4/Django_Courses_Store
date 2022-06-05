from django.shortcuts import render , get_object_or_404 , redirect , resolve_url
from django.http import HttpRequest
from .models import course , Review
from .forms import ReviewForm, RegisterForm , courseform


def home(request):
    context= {'course':course.objects.all()}
    return render(request,'home.html',context)

def course_detail(request, pk):
	namecourse = get_object_or_404(course, pk=pk)
	if request.method == 'POST':
		form = ReviewForm(request.POST)

		if form.is_valid():
			obj = form.save(commit=False)
			obj.namecourse = namecourse
			obj.user = request.user
			obj.save()

			return redirect('course_detail', pk=namecourse.pk)
	else:
		form = ReviewForm()

	context = {
		'namecourse': namecourse,
		'form': form}
	return render(request, 'course_detail.html', context)

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password1'])
			new_user.save()
	else:
		form = RegisterForm()
	return render(request, 'register.html', {
		'title': 'singup',
		'form': form,
	})

def bougth(request:HttpRequest, course_id):
	Bougth=course(request)
	Bougth.add(pk=course_id)
	return render(request,'orders_page.html')


def addcourse(request):
	if request.user.has_perm("courseapp.add_course") and request.user.is_authenticated:
		form = courseform()
		return render(request, 'add_course_page.html', {'form': form})
	else:
		massege = 'You do not have this permission to add a course or try logging in and trying again'
		return render(request, 'add_course_page.html', {'massege': massege})
