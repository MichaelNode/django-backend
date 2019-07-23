from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False) 
    email = models.EmailField(unique=True,null=False)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)

class Menu(models.Model):

    starter = models.CharField(max_length=100, null=False)
    main_course = models.CharField(max_length=100, null=False)
    desserts = models.CharField(max_length=100, null=False)
    menu_date = models.DateTimeField(null=False)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateField(auto_now=True)

class Order(models.Model):

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customization = models.TextField(null=True)
    order_date = models.DateTimeField(null=False)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateField(auto_now=True)

  


