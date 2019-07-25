
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import MyUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class EmployeeList(ListView):
    model = MyUser
    template_name = 'user/list_employee.html'
    context_object_name = 'employees'
    paginate_by = 7

    def get_queryset(self):
        queryset = MyUser.objects.filter(employee=True)
        return queryset


class EmployeeCreate(CreateView):
    model = MyUser
    form_class = CustomUserCreationForm
    template_name = 'user/new_employee.html'
    success_url_text = 'list_employee'

    def get_success_url(self):
        return reverse(self.success_url_text)


class EmployeeUpdate(UpdateView):
    model = MyUser
    form_class = CustomUserChangeForm
    template_name = 'user/edit_employee.html'
    success_url_text = 'list_employee'

    def get_success_url(self):
        return reverse(self.success_url_text)
