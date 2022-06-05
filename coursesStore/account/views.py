from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate ,login,logout
from .forms import LoginForm
# Create your views here.
def reigester(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            return redirect(resolve_url('login'))
    form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login_user(request):

    if request.method == 'POST':
        user_form = LoginForm(request.POST)

        if user_form.is_valid():
            
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            authenticate_user = authenticate(request, username=username, password=password)
            
            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect(resolve_url('home'))
            else:
                return redirect(resolve_url('login'))


    return render(request, 'login.html', {'form' : LoginForm()})

def logout_user(request):
    logout(request)
    return render(request,'logout.html')
