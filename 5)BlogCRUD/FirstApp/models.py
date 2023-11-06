from django.db import models

# Create your models here.
class BlogModel(models.Model):
    blog_name = models.CharField(max_length=30)
    blog_discription = models.TextField()
    blog_image = models.ImageField(upload_to="media")
