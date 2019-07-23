
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Menu
from .forms import MenuForm


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


class MenuList(ListView):
    model = Menu
    template_name = 'main/list_menu.html'
    context_object_name = 'menus'


class MenuDetail(DetailView):
    model = Menu


class MenuCreate(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'main/new_menu.html'
    success_url_text = 'home'

    def get_success_url(self):
        return reverse(self.success_url_text)


class MenuUpdate(UpdateView):
    model = Menu
