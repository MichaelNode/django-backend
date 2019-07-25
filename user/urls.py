# urls.py

from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url('add_employee', login_required(views.EmployeeCreate.as_view()), name="add_employee"),
    url('list_employee', login_required(views.EmployeeList.as_view()), name="list_employee"),
    url('edit_employee/(?P<pk>\d+)', login_required(views.EmployeeUpdate.as_view()), name="edit_employee")
    ]
