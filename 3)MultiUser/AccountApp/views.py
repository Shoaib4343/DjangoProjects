from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .form import StyleRegister,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.

def index_views(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = StyleRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are registered successfully')
            return redirect('/register')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = StyleRegister()
        return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(username=username, password=password)

            if user is not None and user.is_admin:
                login(request, user)
                messages.success(request, 'You are logged in successfully')
                return redirect('/admin_page')
            
            if user is not None and user.is_employee:
                login(request, user)
                messages.success(request, 'You are logged in successfully')
                return redirect('/employee')
            
            if user is not None and user.is_customer:
                login(request, user)
                messages.success(request, 'You are logged in successfully')
                return redirect('/customer')
            else:
                messages.success(request, 'Invalid username or password')
                return redirect('/login')
            
            
            
        # else:
        #     messages.error(request,"Login Failed ...")
        #     return redirect('/login')



    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    # logout(request,user)
    return render(request,'login.html')




def admin_view(request):
    return render(request,'admin.html')

def employee_view(request):
    return render(request,'employee.html')

def customer_view(request):
    return render(request,'customer.html')