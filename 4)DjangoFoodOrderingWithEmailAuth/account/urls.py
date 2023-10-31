from django.contrib import admin
from django.urls import path
from account.views import *

urlpatterns = [
    path('',index_page, name='index'),
    path('index/',index_page, name='index'),
]