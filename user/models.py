# user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):

    employee = models.BooleanField(default=True)
    country = models.CharField(max_length=100, null=False)
    jobs = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
