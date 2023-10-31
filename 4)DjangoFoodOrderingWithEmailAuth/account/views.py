from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
# User = get_user_model
def index_page(request):
    return render(request, 'index.html')