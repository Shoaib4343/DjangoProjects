from django.shortcuts import render,redirect,HttpResponse
from .models import BlogModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index_page(request):
    if request.method == "POST":    
        data = request.POST
        blog_name = data.get('blog_name')
        blog_discription = data.get('blog_discription')
        blog_image = request.FILES.get('blog_image')

        BlogModel.objects.create(
            blog_name=blog_name,
            blog_discription = blog_discription,
            blog_image = blog_image,
        )
        return redirect('/index')

    queryset = BlogModel.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(blog_name__icontains=request.GET.get('search'))

        

    return render(request, "blog.html",{'queryset':queryset})


def delete_blog(request, id):
    queryset = BlogModel.objects.get(id=id)
    queryset.delete()
    return redirect('/index')

def update_blog(request, id):
    queryset = BlogModel.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        blog_name = data.get('blog_name')
        blog_discription = data.get('blog_discription')
        blog_image = request.FILES.get('blog_image')

        queryset.blog_name = blog_name
        queryset.blog_discription = blog_discription

        if blog_image:
            queryset.blog_image = blog_image
        queryset.save()
        return redirect('/index')
    
    return render(request, 'update_blog.html', {'queryset': queryset})



#Registrations Form
def register_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, "User Exists")

        else:
            user = User.objects.create(
                username=username,
                first_name = first_name,
                last_name = last_name,
            )
            user.set_password(password)
            user.save()
            messages.success(request, 'Registeration successfully')
            return redirect('/register')

    return render(request, 'register.html')

# Login Form
def Login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.warning(request, 'Invalide Username ')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, 'Invalide Password ')
        else:
            messages.success(request,'login successful')
            return redirect('/index')
            
    return render(request, 'login.html')

