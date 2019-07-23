# urls.py

from django.conf.urls import url
from .views import LoginView, LogoutView

urlpatterns = [
    url(
        regex = r'^login/$',
        view  = LoginView.as_view(),
        name  = "panel-login"),
    url(
        regex = r'^logout/$',
        view  = LogoutView.as_view(),
        name  = "panel-logout"),
    ]
