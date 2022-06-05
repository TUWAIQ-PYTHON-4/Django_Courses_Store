from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .forms import RegistrationForm


# Create your views here.

def home(request: HttpRequest):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

