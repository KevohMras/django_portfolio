from django.db import models

# Create your models here.

class Portfolio(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    second_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    number = models.IntegerField(max_length=30, blank=False)
    image = models.ImageField(upload_to="uploads/images", default="uploads/images/profile.jpg")

