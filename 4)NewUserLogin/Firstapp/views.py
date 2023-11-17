from django.shortcuts import render,HttpResponse,redirect
from .form import RegisterForm,LoginForm,UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_page(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register successfully...")
            return redirect('/index')
        else:
            form = RegisterForm(request.POST)
            return render(request, 'register.html/',{'form':form})
    form = RegisterForm()
    return render(request, 'register.html/',{'form':form})




def login_page(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request,user)
                # messages.success(request,"Login successfully...")
                # return redirect("/dashboared")
                return redirect('/profile')
            else:
                messages.error(request,"Login Failed ...")
                return redirect('/login')
                # return HttpResponse("Login fail")

    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form})



def logout_page(request):
    logout(request)
    return redirect('/login')


def index_page(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'index.html')


# Dashboard routes

# Profile page

def dash_index_page(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    form = UserProfile(instance = request.user)
    return render(request, 'dashboard/dash_index.html', {'form': form})


