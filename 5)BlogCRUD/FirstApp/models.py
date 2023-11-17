from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    blog_name = models.CharField(max_length=30)
    blog_discription = models.TextField()
    blog_image = models.ImageField(upload_to="media",blank=True, null=True)
