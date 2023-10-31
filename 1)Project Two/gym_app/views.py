from django.shortcuts import render,redirect,HttpResponse
from .form import RegistraionForm,StyleLogin,UserProfile,UserProfileUpdate,ChnagePassword
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash



# Create your views here.

#idnex 
def index_page(request):
    return render(request, 'index.html')



#registration

def registration_page(request):
    if  request.user.is_authenticated:
        return redirect("/dashboared")
    if request.method == "POST":
        form = RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            # user_data = form.cleaned_data
            # new_user = ModelRegistration.objects.create(
            #     username=user_data['username'],
            #     first_name=user_data['first_name'],
            #     last_name=user_data['last_name'],
            #     email=user_data['email'],
            #     password1 = user_data['password1'],
            #     password2 = user_data['password2'],
            # )
            # new_user.save()

           
            messages.success(request,"Acount Created Successfully...")
            return redirect('registration')
        else:
           
            return render(request,'registration.html',{"form":form})
    

    else:
        form = RegistraionForm()
    return render(request,'registration.html',{"form":form})





#login
def login_page(request):
    if  request.user.is_authenticated:
        return redirect("/dashboared")
    if request.method == 'POST':
        form = StyleLogin(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully...")
                return redirect("/dashboared")
            else:
                messages.error(request,"Login Failed ...")
                return redirect('/login')

    else:
        form = StyleLogin()
    return render(request, 'login.html',{'form':form})

#logout

def logout_page(request):
    if not request.user.is_authenticated:
        return redirect("/index")
    logout(request)
    
    return redirect("/index")

#dashboard
def dashboared_page(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request,'dashboard/dash_index.html')

#Profile 
def profile_page(request):
    if not request.user.is_authenticated:
        return redirect("/index")
    
    form = UserProfile(instance = request.user)
    return render(request,'dashboard/profile.html',{'form':form})
    



#update Profile

def profile_update_page(request):
    if not request.user.is_authenticated:
        return redirect("/index")
    
    if request.method == 'POST':
        form = UserProfileUpdate(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Udatation successfully...')
            return redirect('/profile')
        
        else:
           
           return render(request,'dashboard/profile.html',{'form':form}) 
    else:
        form = UserProfileUpdate(instance = request.user)
        return render(request,'dashboard/UpdateProfile.html',{'form':form})







# delete profile
def profile_delele_page(request):
    if not request.user.is_authenticated:
        return redirect("/index")
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.success(request,'Account Deleted Successfully...')
        return redirect('/index')
    return render(request,'dashboard/DeleteProfile.html')



#change Password
def change_password_page(request):
    if not request.user.is_authenticated:
        return redirect("/index")
    if request.method == 'POST':
        change_pass = ChnagePassword(user=request.user, data=request.POST)
        if change_pass.is_valid():
            change_pass.save()
            messages.success(request,'Password Change Successfully...')
            update_session_auth_hash(request, change_pass.user)
            return redirect('/dashboared')
        else:
            
            return render(request,'dashboard/change_pass.html',{'change_pass':change_pass})
    else:
        change_pass = ChnagePassword(user = request.user)
        return render(request,'dashboard/change_pass.html',{'change_pass':change_pass})