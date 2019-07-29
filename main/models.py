from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from cornershop import settings


class Menu(models.Model):

    starter = models.CharField(max_length=100, null=False)
    main_course = models.CharField(max_length=100, null=False)
    desserts = models.CharField(max_length=100, null=False)
    menu_date = models.DateTimeField(null=False)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s Y %s" % (self.main_course, self.starter, self.desserts)


class Order(models.Model):

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customization = models.TextField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

  


