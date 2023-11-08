from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from RecipyApp.seed import *
# Create your views here.


def recipe_page(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method == "POST":
        form = request.POST
        recipe_name = form.get('recipe_name')  # get the recipe data form the form and store it in the respective variables
        recipe_discription = form.get('recipe_discription')
        recipe_image = request.FILES.get('recipe_image')

        RecipeModel.objects.create( # create the object for the recipe in the database and store the variables in the model data
            recipe_name = recipe_name,
            recipe_discription = recipe_discription,
            recipe_image = recipe_image,
        )
        return redirect("/recipe")
    
    queryset = RecipeModel.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))

    return render(request,'recipe.html',{queryset:'queryset'})


def delete_recipe_page(request,id):
    if not request.user.is_authenticated:
        return redirect("/login")
    query = RecipeModel.objects.get(id=id)
    query.delete()
    return redirect("/recipe")

def update_recipe_page(request,id):
    if not request.user.is_authenticated:
        return redirect("/login")
    query = RecipeModel.objects.get(id=id)
    if request.method == "POST":
        recipe = request.POST
        recipe_name = recipe.get('recipe_name')
        recipe_discription = recipe.get('recipe_discription')
        recipe_image = request.FILES.get('recipe_image')

        query.recipe_name = recipe_name
        query.recipe_discription = recipe_discription
        if recipe_image:
            query.recipe_image = recipe_image
        query.save()
        return redirect('/recipe')
        
    return render(request, 'update_recipe.html',{'query':query})

 #registration form
def register_page(request):
    if request.user.is_authenticated:
        return redirect("/recipe")
    if request.method == "POST":
        username = request.POST.get('username')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        password= request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.warning(request, "This username is already taken. Please different one.")
            return redirect('/register')
        else:
            user = User.objects.create(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
            )
            user.set_password(password)
            user.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect("/register")
    return render(request,'register.html')

# login page
def login_page(request):
    if request.user.is_authenticated:
        return redirect("/recipe")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            messages.warning(request,"invalid username")
            return redirect("/login")
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.warning(request,"invalid password")
            return redirect("/login")
        else:
            login(request,user)
            messages.success(request,"Login successfuly")
            return redirect("/recipe")
        
    return render(request,'login.html')

# logout page

def logout_page(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    logout(request)
    return redirect("/login")


def report_card_views(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search)|
            Q(student_id__student_id__icontains = search) |
            Q(department__department__icontains = search)|
            Q(student_email__icontains = search)|
            Q(student_address__icontains = search)|
            Q(student_age__icontains = search)
            
            )



    paginator = Paginator(queryset, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'ReoportCard/report.html',{"queryset":page_obj})


def see_marks_view(request, student_id):
    queryset = StudentMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    return render(request,'ReoportCard/sum_marks.html',{"queryset":queryset, 'total_marks':total_marks})



