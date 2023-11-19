from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
   

class UserProfile(UserChangeForm):
    password = None
    username = forms.CharField(max_length=30 ,disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=30,disabled=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdateProfile(UserChangeForm):
    password = None
    username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class PassChnage(PasswordChangeForm):
    old_password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
   
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']