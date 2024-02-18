from django.shortcuts import render
from .models import user

# Create your views here.
def home(request):
    users = user.objects.all()
    hmhm = 'gdgfngh'
    return render(request, 'home.html', { 'users' : users , 'hmhm' : hmhm})

def login(request):
    return render(request, 'login.html', {})