from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import *
from .models import *
from django import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import user
import random
import string


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        emailu = request.POST.get('email')
        passwordu = request.POST.get('password')
        print(emailu)
        print(passwordu)
        user = authenticate(request, username=emailu, password=passwordu)
        if user is not None:
            login(request, user)
            messages.success(request, 'welcome to ALG ON')
            return redirect('home')
        else:
            messages.success(request, 'please try again')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'you have logged out')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = infoForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        if password1 != password2:
            form = infoForm()
            return render(request, 'register.html', {'error': 'Passwords do not match.'}, {'form': form})
        else:
           if form.is_valid():
               username = f"{name} {form.cleaned_data['last_name']}"
           #unique_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
           #username = f"{full_name}_{unique_id}"
           #v = validate_email(email, verify=True)
           v = 1
           if v:
              if User.objects.filter(email=email).exists():
                  return render(request, 'register.html', {'error': 'Email address already in use.'}, {'form': form})
              else:
                  user = User.objects.create_user(username=username, email=email, password=password1)
                  user.save()
                  if user and form.is_valid():
                    new_info = info(user=user, last_name=form.cleaned_data['last_name'], address=form.cleaned_data['address'], phone=form.cleaned_data['phone'])
                    new_info.save()
                    login(request, user)
                    return redirect('home')    
           else:
               form = infoForm()
               return render(request, 'register.html', {'error': 'Email address does not exist.'}, {'form': form})
    else:
        print("7")
        form = infoForm()
        return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    @user_passes_test(lambda u: u.is_authenticated, login_url='login')
    def view(request):
      users = user.objects.all()
      hmhm = 'gdgfngh'
      return render(request, 'home.html', { 'users' : users , 'hmhm' : hmhm})
    return view(request)

@login_required
def update_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prename = request.POST.get('prename')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
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
                #Uinfo = info.objects.get(user=current_user)
                try:
                   Uinfo = info.objects.get(user=current_user)
                   Uinfo.last_name = prename
                   Uinfo.address = address
                   Uinfo.phone=phone
                   Uinfo.save()
                   print("uinfo exists")
                except info.DoesNotExist:
                   new_info = info(user=current_user, last_name=prename, address=address, phone=phone)
                   new_info.save()
                   print("uinfo does not exist")
                
                return redirect('home')
    else:
        return render(request, 'update_user.html', {})
    
@login_required
def create_cv(request):
    form = infoForm
    return render(request, 'create_cv.html', {'form': form})

def del_user(request):
    try:
        User.objects.exclude(id=1).delete()
    except User.DoesNotExist:
        pass


    #userr = User.objects.get(id=1)
    #login(request, userr)
    #messages.success(request, 'welcome to ALG ON')
    #return redirect('home')
    return redirect('login')