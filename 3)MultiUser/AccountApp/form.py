from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class StyleRegister(UserCreationForm):
    username= forms.CharField(max_length=100,error_messages={'required':'*UserName Required'} ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(error_messages={'required':'*Email Required'} ,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(max_length=100,error_messages={'required':'*Password Required'} ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(max_length=100,error_messages={'required':'*Conform'} ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_admin = forms.BooleanField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}),initial=True)
    is_employee = forms.BooleanField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}),initial=False)
    is_customer = forms.BooleanField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}),initial=False)
    # role= forms.ChoiceField(widget=forms.RadioSelect(),choices=(('admin', 'Admin'),('customer', 'Customer'),('employee', 'Employee')))



    class Meta:
        model=User
        fields=('username','email','password1','password2','is_admin','is_employee','is_customer')


class LoginForm(forms.Form):
    username= forms.CharField(max_length=100,error_messages={'required':'*UserName Required'},widget=forms.TextInput(attrs={'class': 'form-control'}))
    password= forms.CharField(max_length=100,error_messages={'required':'*Password Required'},widget=forms.PasswordInput(attrs={'class': 'form-control'}))