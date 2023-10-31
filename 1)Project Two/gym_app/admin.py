from django.contrib import admin
from .models import ModelRegistration

# Register your models here.
@admin.register(ModelRegistration)
class AdminRegistration(admin.ModelAdmin):
    list_display = ('id','username','first_name','last_name','email','password1','password2')



