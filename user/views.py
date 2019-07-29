from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
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
        if self.request.user.is_superuser:
            return MyUser.objects.filter(employee=True)
        else:
            raise PermissionDenied()


class EmployeeCreate(CreateView):
    model = MyUser
    form_class = CustomUserCreationForm
    template_name = 'user/new_employee.html'
    success_url_text = 'list_employee'

    def get_success_url(self):
        return reverse(self.success_url_text)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            if self.request.user.is_superuser:
                new_employee = form.save()
                messages.success(
                    request,
                    'Employee {0} created successfully!'.format(new_employee.username)
                )
                return HttpResponseRedirect(reverse(self.success_url_text))
            else:
                messages.warning(
                    request,
                    'Only administrators can create a employee'
                )
        return render(request, 'user/new_employee.html', {'form': form})


class EmployeeUpdate(UpdateView):
    model = MyUser
    form_class = CustomUserChangeForm
    template_name = 'user/edit_employee.html'
    success_url_text = 'list_employee'

    def get_success_url(self):
        return reverse(self.success_url_text)

    def get_object(self):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EmployeeUpdate, self).get_object()
        if not self.request.user.is_superuser:
            raise Http404
        return obj


class EmployeeDetail(DetailView):
    model = MyUser
    template_name = 'user/details_employee.html'
    context_object_name = 'employee'

    def get_object(self):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EmployeeDetail, self).get_object()
        if not self.request.user.is_superuser:
            raise Http404
        return obj


class EmployeeDelete(DeleteView):
    model = MyUser
    template_name = 'user/delete_employee.html'
    success_url_text = 'list_employee'

    def get_success_url(self):
        return reverse(self.success_url_text)

    def get_object(self):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EmployeeDelete, self).get_object()
        if not self.request.user.is_superuser:
            raise Http404
        return obj
