
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.home, name="home_min"),
    path('addmenu', login_required(views.MenuCreate.as_view()), name="menu"),
    path('menu', login_required(views.MenuList.as_view()), name="home"),
    path('order', views.home, name="order"),

]





