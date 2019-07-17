from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):

    emp_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_lenght=100, null=False)
    last_name = models.CharField(max_lenght=100, null=False) 
    email = models.EmailField(unique=True,null=False)
    date_reg = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return '{0}'.format(self.name)

class Menu(models.Model):

    menu_id = models.BigAutoField(primary_key=True)
    starter = models.CharField(max_lenght=100, null=False)
    main_course = models.CharField(max_lenght=100, null=False)
    desserts = models.CharField(max_lenght=100, null=False)
    manu_date = models.DateTimeField(null=False) 
    date_reg = models.DateTimeField(auto_now_add=True) 

    


