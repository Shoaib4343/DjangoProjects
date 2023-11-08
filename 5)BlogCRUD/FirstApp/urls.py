from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index_page, name='index'),
    path('index/',index_page, name='index'),

    # delete
    path('delete_blog/<id>', delete_blog, name='delete_blog'),

    # Update
    path('update_blog/<id>', update_blog, name='update_blog'),

    # Regster and 
    path('register/', register_form, name='register'),
    path('login/', Login_form, name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
