from django.contrib import admin
from django.urls import path
from RecipyApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',register_page, name='register'),
    path('recipe/',recipe_page, name='recipe'),
    path('delete_recipe/<id>',delete_recipe_page,name='delete_recipe'),
    path('update_recipe/<id>', update_recipe_page, name='update_recipe'),

    #register and login
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),

    #report card
    path('report/', report_card_views, name='report'),
    path('see_marks/<student_id>', see_marks_view, name='see_marks'),
    
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
