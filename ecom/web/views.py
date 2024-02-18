from django.shortcuts import render
from .models import user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    users = user.objects.all()
    hmhm = 'gdgfngh'
    return render(request, 'home.html', { 'users' : users , 'hmhm' : hmhm})

def login_user(request):
    return render(request, 'login.html', {})

def logout_user(request):
    return render(request, 'login.html', {})