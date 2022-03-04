from django.db import models

# Create your models here.

class Registered_Users(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    Username=models.CharField(max_length=20)


class Admin(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
