from django.shortcuts import redirect, render, resolve_url
from .forms import UserCreationForm, UserFormLogin
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,"you are register")
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request,'account/register.html',{'form':form,})


def login_user(request):
    if request.method == 'POST':
        user_form = UserFormLogin(request.POST)

        if user_form.is_valid():

            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            authenticate_user = authenticate(request, username=username, password=password)

            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect('home')
            else:
                return redirect('login')

    return render(request, 'account/login.html', {'form': UserFormLogin()})