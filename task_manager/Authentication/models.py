from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    


    
    def __str__(self):
        return self.username