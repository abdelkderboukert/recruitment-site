from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import SignUpForm
from django import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import user

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        emailu = request.POST.get('email')
        passwordu = request.POST.get('password')
        user = authenticate(request, username=emailu, password=passwordu)
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

import random
import string

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prename = request.POST.get('prename')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})

        full_name = f"{name} {prename}"
        unique_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        username = f"{full_name}_{unique_id}"

        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email address already in use.'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'register.html')

@login_required(login_url=('login/'))
def home(request):
    @user_passes_test(lambda u: u.is_authenticated, login_url='login')
    def view(request):
      users = user.objects.all()
      hmhm = 'gdgfngh'
      return render(request, 'home.html', { 'users' : users , 'hmhm' : hmhm})
    return view(request)

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

@login_required(login_url=('login/'))
def update_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prename = request.POST.get('prename')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        current_user = request.user
        print(current_user.username)
        if User.objects.filter(email=email).exclude(id=current_user.id).exists():
            return render(request, 'update_user.html', {'error': 'Email address already in use.'})
        else:
            full_name = name + " " + prename
            current_user.username = full_name
            current_user.email = email
            if password1 and password1 == password2:
                current_user.set_password(password1)
                update_session_auth_hash(request, current_user)
                current_user.save()
                return redirect('home')
    else:
        return render(request, 'update_user.html', {})