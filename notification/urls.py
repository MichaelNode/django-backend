from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url('send_notification',
        login_required(views.GenerateSendNotification.as_view()),
        name="notification"),
    ]
