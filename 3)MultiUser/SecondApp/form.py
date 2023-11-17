from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    class Meta:
        
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']