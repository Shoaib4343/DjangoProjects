from django.urls import path
from .views import *

urlpatterns = [
    path('',register_page,name='register'),
    path('register/',register_page,name='register'),
    path('index/',index_page,name='index'),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),

    # Dashboard routes Profile
    path('profile/', dash_index_page, name='profile'),
    path('profile_update/', update_user_profile, name='profile_update'),   # Update User
    path('profile_delete/', profile_delete_page, name='profile_delete'),   # Delete User
    path('change_password/', change_password_page, name='change_password'), # Change Password
]
