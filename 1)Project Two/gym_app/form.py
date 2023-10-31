from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm

class RegistraionForm(UserCreationForm):
    username = forms.CharField(max_length=50,error_messages={'*required':'enter your UserName'},widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,error_messages={'*required':'enter your First Name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,error_messages={'*required':'enter your Last Name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(error_messages={'*required':'enter your Email'},widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=50,error_messages={'*required':'enter your Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=50,error_messages={'*required':'Conform Your Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class StyleLogin(AuthenticationForm):
    username = forms.CharField(max_length=50,error_messages={'*required':'enter your UserName'},widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=50,error_messages={'*required':'enter your Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UserProfile(UserChangeForm):
    password = None

    username = forms.CharField(max_length=50,error_messages={'*required':'enter your UserName'},widget=forms.TextInput(attrs={'class':'form-control' ,'disabled': True}))
    first_name = forms.CharField(max_length=50,error_messages={'*required':'enter your First Name'},widget=forms.TextInput(attrs={'class':'form-control','disabled': True}))
    last_name = forms.CharField(max_length=50,error_messages={'*required':'enter your Last Name'},widget=forms.TextInput(attrs={'class':'form-control','disabled': True}))
    email = forms.EmailField(error_messages={'*required':'enter your Email'},widget=forms.EmailInput(attrs={'class':'form-control','disabled': True}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class UserProfileUpdate(UserChangeForm):
    password = None
    username = forms.CharField(max_length=50,error_messages={'*required':'enter your UserName'},widget=forms.TextInput(attrs={'class':'form-control' }))
    first_name = forms.CharField(max_length=50,error_messages={'*required':'enter your First Name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,error_messages={'*required':'enter your Last Name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(error_messages={'*required':'enter your Email'},widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',]

class ChnagePassword(PasswordChangeForm):
    old_password = forms.CharField(max_length=50,error_messages={'*required':'*Enter Your Old Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(max_length=50,error_messages={'*required':'*Enter Your New Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(max_length=50,error_messages={'*required':'*Conform Your Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
