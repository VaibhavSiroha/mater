from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Users(AbstractUser):
    bio=models.TextField(blank=True)
    age=models.PositiveBigIntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10,choices=[('M','Male'),('F','Female'),('O','Others')],blank=True)
    location=models.CharField(max_length=200,blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True,null=True)


    def __str__(self):
        return self.username
    

