from django.shortcuts import render, redirect
from .models import user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    users = user.objects.all()
    hmhm = 'gdgfngh'
    return render(request, 'home.html', { 'users' : users , 'hmhm' : hmhm})

def login_user(request):
    #if request.user.is_authenticated:
    #    return redirect('home')
    if request.method == 'POST':
        emailu = request.POST.get('email')
        passwordu = request.POST.get('password')
        user = authenticate(request, email=emailu, password=passwordu)
        if user is not None:
            login(request, user)
            messages.success(request, 'welcome to ALG ON')
            return redirect('home')
        else:
            messages.success(request, 'please try again')
            return redirect('home')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'you have logged out')
    return redirect('login')

def register(request):
    return render(request, 'register.html', {})