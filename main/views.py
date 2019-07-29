from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Menu, Order
from .forms import MenuForm, MenuEditForm, OrderForm, OrderEditForm
from django.utils.timezone import localtime


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


class MenuList(ListView):
    model = Menu
    template_name = 'main/list_menu.html'
    context_object_name = 'menus'
    paginate_by = 7

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Menu.objects.all().order_by('-menu_date')
        else:
            raise PermissionDenied()


class MenuListToday(ListView):
    model = Menu
    template_name = 'main/today_menu.html'
    context_object_name = 'menus'
    paginate_by = 7

    def get_queryset(self):
        return Menu.objects.filter(menu_date=localtime().date())


class MenuDetail(DetailView):
    model = Menu
    template_name = 'main/details_menu.html'


class MenuDelete(DeleteView):
    model = Menu
    template_name = 'main/delete_menu.html'
    success_url_text = 'home'

    def get_success_url(self):
        return reverse(self.success_url_text)

    def get_object(self):
        """ Hook to ensure object is owned by request.user. """
        obj = super(MenuDelete, self).get_object()
        if not self.request.user.is_superuser:
            if not obj.owner == self.request.user:
                raise Http404
        return obj


class MenuCreate(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'main/new_menu.html'
    success_url_text = 'home'

    def get_success_url(self):
        return reverse(self.success_url_text)

    def post(self, request):
        # get request.user and add form
        new_menu = Menu(owner=request.user)
        form = MenuForm(request.POST, instance=new_menu)
        if form.is_valid():
            if self.request.user.is_superuser:
                new_menu = form.save()
                messages.success(
                    request,
                    'Menu {0} created successfully!'.format(new_menu.starter)
                )
                return HttpResponseRedirect(reverse(self.success_url_text))
            else:
                messages.warning(
                    request,
                    'Only administrators can create a menu'
                )
        return render(request, 'main/new_menu.html', {'form': form})


class MenuUpdate(UpdateView):
    model = Menu
    form_class = MenuEditForm
    template_name = 'main/edit_menu.html'
    success_url_text = 'home'

    def get_success_url(self):
        return reverse(self.success_url_text)

    def get_object(self):
        # Hook to ensure object is owned by request.user.
        obj = super(MenuUpdate, self).get_object()
        if not self.request.user.is_superuser:
            if not obj.owner == self.request.user:
                raise Http404
        return obj


# views of Order.
class OrderList(ListView):
    model = Order
    template_name = 'main/list_order.html'
    context_object_name = 'orders'
    paginate_by = 7

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all().order_by('-order_date')
        else:
            return Order.objects.\
                filter(employee=self.request.user).order_by('-order_date')


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'main/new_order.html'
    success_url_text = 'order_list'

    def post(self, request):
        new_order = Order(employee=request.user)
        form = OrderForm(request.POST, instance=new_order)
        if form.is_valid():
            if Order.objects.\
                    filter(employee=request.user,
                           order_date__date=localtime().date()).exists():
                messages.warning(
                    request,
                    'The order has already been made'.format(new_order.menu)
                )
            else:
                new_order = form.save()
                messages.success(
                    request,
                    'Order {0} created successfully!'.format(new_order.menu)
                )
                return HttpResponseRedirect(reverse(self.success_url_text))
        return render(request, 'main/new_order.html', {'form': form})


class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderEditForm
    template_name = 'main/edit_order.html'
    success_url_text = 'order_list'

    def get_success_url(self):
        return reverse(self.success_url_text)


class OrderDetail(DetailView):
    model = Order
    template_name = 'main/details_order.html'
    context_object_name = 'order'


class OrderDelete(DeleteView):
    model = Order
    template_name = 'main/delete_order.html'
    success_url_text = 'order_list'

    def get_success_url(self):
        return reverse(self.success_url_text)

    def get_object(self):
        # Hook to ensure object is owned by request.user.
        obj = super(OrderDelete, self).get_object()
        if not self.request.user.is_superuser:
            if not obj.employee == self.request.user:
                raise Http404
        return obj
