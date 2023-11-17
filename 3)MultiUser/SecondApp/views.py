from django.shortcuts import render,redirect,HttpResponse
from .form import CustomRegistrationForm

# Create your views here.

def new_register_page(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/new_register')
        else:
            return render(request, 'new_register.html', {'form': form})
        
    form = CustomRegistrationForm()
    return render(request, 'new_register.html',{'form': form})

def new_login_page(request):
    return render(request, 'new_login.html')