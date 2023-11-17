from django.urls import path,include
from .views import *

urlpatterns = [
    path('', new_register_page, name='new_register'), #this shoudl be an empty path
    path('new_register/', new_register_page, name='new_register'),
    path('new_login/', new_login_page, name='new_login'),
    

]
