
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.home, name="home_main"),
    path('add_menu', login_required(views.MenuCreate.as_view()), name="menu"),
    path('edit_menu/<int:pk>', login_required(views.MenuUpdate.as_view()), name="menu_edit"),
    path('today_menu', views.MenuListToday.as_view(), name="menu_today"),
    path('menu', login_required(views.MenuList.as_view()), name="home"),
    path('orders', login_required(views.OrderList.as_view()), name="order_list"),
    path('add_order', login_required(views.OrderCreate.as_view()), name="order_add"),
    path('edit_order/<int:pk>', login_required(views.OrderUpdate.as_view()), name="order_edit"),

]





