from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin= models.BooleanField('Is Admin',default=False)
    is_customer= models.BooleanField('Is Customer',default=False)
    is_employee= models.BooleanField('Is Employee',default=False)
    

# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('admin', 'Admin'),
#         ('customer', 'Customer'),
#         ('employee', 'Employee'),
#     )

#     user_type = models.CharField('User Type', max_length=10, choices=USER_TYPE_CHOICES, default='customer')

#     def is_admin(self):
#         return self.user_type == 'admin'

#     def is_customer(self):
#         return self.user_type == 'customer'

#     def is_employee(self):
#         return self.user_type == 'employee'

    