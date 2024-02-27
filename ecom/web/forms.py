from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import info

class infoForm(forms.ModelForm):
    last_name = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={'class':'put-on', 'placeholder':'Last Name'}))
    age = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class':'put-on', 'placeholder':'Age'}))
    address = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class':'put-on', 'placeholder':'Address'}))
    phone = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={'class':'put-on', 'placeholder':'Phone Number'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'put-on', 'type':'date'}))
    
    class Meta:
        model = info
        fields = ["last_name", "age", "address", "phone", "date"]
