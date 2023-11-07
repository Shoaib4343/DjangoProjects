from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# class ModelManager(models.Manager):
#     def get_queryset(self) -> QuerySet:
#         return super().get_queryset().filter(is_deleted=True)

class StudentManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=True)
class RecipeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null= True)
    recipe_name = models.CharField(max_length=100)
    recipe_discription = models.TextField()
    recipe_image = models.ImageField(upload_to='images',null=True, blank=True)
    recipe_viws_count = models.IntegerField(default=1)
    # is_deleted = models.BooleanField(default=False)

    # objects=ModelManager()
    # admin_objects = models.Manager()

   

class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_address = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    is_deleted = models.BooleanField(default=False)

    objects = StudentManager()
    admin_objects = models.Manager()
    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name


class StudentMarks(models.Model):
    student = models.ForeignKey(Student, related_name="Studnet_marks_with_realte_name", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='subjects_with_realalted_name', on_delete=models.CASCADE)
    marks = models.IntegerField()
   
    def __str__(self) -> str:
        return  f'{self.student.student_name} {self.subject.subject_name}'

    class Meta:
        unique_together = ['subject', 'student']
    