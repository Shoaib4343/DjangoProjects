from django.shortcuts import render,redirect,HttpResponse
from .models import BlogModel

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
        

    return render(request, "blog.html",{'queryset':queryset})


def delete_blog(request, id):
    queryset = BlogModel.objects.get(id=id)
    queryset.delete()
    return redirect('/index')
