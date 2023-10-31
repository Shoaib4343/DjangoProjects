from django.contrib import admin
from django.urls import path
from AccountApp.views import *

urlpatterns = [
    path('',register_view, name='register'),
    path('index/',index_views, name='indedx'),
    path('register/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),

    path('customer/',customer_view, name='customer'),
    path('employee/',employee_view, name='employee'),
    path("admin_page/",admin_view, name='admin_page'),

]
