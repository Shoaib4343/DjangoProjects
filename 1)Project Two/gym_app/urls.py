from django.contrib import admin
from django.urls import path
from gym_app import views

urlpatterns = [
    path('',views.index_page , name='index'),
    path('index/',views.index_page , name='index'),
    path('registration/',views.registration_page , name='registration'),
    path('login/',views.login_page , name='login'),
    path('logout/',views.logout_page , name='logout'),
    # dashboard
    path('dashboared/',views.dashboared_page , name='dashboared'),

    # profile
    path('profile/',views.profile_page, name='profile'),
    path('profile_update/',views.profile_update_page, name='profile_update'),
    path('profile_delele/',views.profile_delele_page, name='profile_delele'),
    path('change_password/',views.change_password_page,name='change_password_page'),

]
