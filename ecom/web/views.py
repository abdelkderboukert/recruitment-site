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
from django.http import HttpResponse
from django.http import JsonResponse 
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
                  user = User.objects.create_user(username=username, email=email, password=password1, first_name=name, last_name=form.cleaned_data['last_name'])
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
      jobs = job.objects.all()
      current_user= request.user
      Uinfo = info.objects.get(user=current_user)
      Ujobs = Uinfo.jobs.all()
      i=0
      n=0
      for k in jobs:
          if k in Ujobs:
              print(k.name)
              i=i+1
              
          n=i+1
          
      for k in jobs:
          print(k.name)
        
      print(i)
      print(n)
      return render(request, 'home.html', { 'jobs' : jobs , 'Ujobs' : Ujobs})
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
            current_user.first_name = name
            current_user.last_name = prename
            if password1 and password1 == password2:
                current_user.set_password(password1)
                update_session_auth_hash(request, current_user)
                current_user.save()
                try:
                   Uinfo = info.objects.get(user=current_user)
                   Uinfo.last_name = prename
                   Uinfo.address = address
                   Uinfo.phone=phone
                   Uinfo.save()
                except info.DoesNotExist:
                   print("5")
                   new_info = info(user=current_user, last_name=prename, address=address, phone=phone)
                   new_info.save()
                
                return redirect('home')
    else:
        print("6")
        current_user = request.user
        Uinfo = info.objects.get(user=current_user)
        context = {'user': current_user,
                   'name': current_user.last_name,
                   'prename': Uinfo.last_name,
                   'email': current_user.email,
                   'address': Uinfo.address if current_user else '',
                   'phone': Uinfo.phone if current_user.info else ''}
        return render(request, 'update_user.html', context)
    
@login_required
def create_cv(request):
    users = [1,2,3,4,5]
    return render(request, 'create_cv.html', {'users':users})

@login_required
def add(request, jobID):
        current_user = request.user
        jobb = job.objects.get(id=int(jobID))
        Uinfo = info.objects.get(user=current_user)
        Uinfo.jobs.add(jobb)
        Uinfo.save()
        return JsonResponse({'status':'success'})

def del_user(request):
    try:
        User.objects.exclude(id=1).delete()
    except User.DoesNotExist:
        pass

    #c = condition(age=25)
    #c.save()
    #j = job(name='frontend DEV', details='', salary=725, condition=c)
    #j.save()

    #userr = User.objects.get(id=1)
    #login(request, userr)
    #messages.success(request, 'welcome to ALG ON')
    #return redirect('home')
    return redirect('login')