from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, login
from .forms import registerforms, UserFormLogin


def register(request):
    form=registerforms()
    if request.method =='POST':
        form = registerforms(request.POST)
        if form.is_valid():
            user =form.save()
            auth_login(request,user)
            return redirect('base')

    return render(request,'register.html',{'form':form})


def login_user(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserFormLogin(request.POST)

        if user_form.is_valid():

            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            authenticate_user = authenticate(request, username=username, password=password)

            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect('index')
            else:
                return redirect('login')

    return render(request, 'login.html', {'form': UserFormLogin()})
