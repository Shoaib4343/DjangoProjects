from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(RecipeModel)
# class recipeAdmin(admin.ModelAdmin):
#     list_display = ('recipe_name','recipe_discription','recipe_image')

admin.site.register(RecipeModel)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)
class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']   

admin.site.register(StudentMarks, StudentMarksAdmin)

