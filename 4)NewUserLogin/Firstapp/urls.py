from django.urls import path
from .views import *

urlpatterns = [
    path('',register_page,name='register'),
    path('register/',register_page,name='register'),
    path('index/',index_page,name='index'),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),

    # Dashboard routes
    path('profile/', dash_index_page, name='profile'),
]
