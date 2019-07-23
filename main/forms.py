from django import forms

from main.models import Menu,Order


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ['starter', 'main_course', 'desserts', 'menu_date']
        widgets = {
             'menu_date': forms.TextInput(attrs={'type': 'date'}),
        }

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['menu', 'customization']

        widgets = {
             'menu': forms.Select(),
             'act_descrip': forms.Textarea(),
        }
