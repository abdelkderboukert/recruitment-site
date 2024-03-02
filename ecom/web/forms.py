from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import info

class infoForm(forms.ModelForm):
    last_name = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={'class':'put-to', 'placeholder':'prename', 'name':'prename'}))
    #age = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class':'put-to', 'placeholder':'Age'}))
    address = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class':'put-to', 'placeholder':'Address', 'name':'address'}))
    phone = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={'class':'put-to', 'placeholder':'N°phon', 'name':'phone'}))
    #date = forms.DateField(widget=forms.DateInput(attrs={'class':'put-to', 'type':'date'}))
    
    class Meta:
        model = info
        fields = ["last_name", "address", "phone"]
