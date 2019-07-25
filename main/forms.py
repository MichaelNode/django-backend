from django import forms
from main.models import Menu, Order
from django.utils.timezone import localtime


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['starter', 'main_course', 'desserts', 'menu_date']
        widgets = {
            'menu_date': forms.TextInput(attrs={'type': 'date', 'required': 'true'}),
        }

    def clean(self):
        data = self.cleaned_data
        date_validation = localtime().replace(hour=11, minute=0, second=0, microsecond=0)
        if data.get('menu_date'):
            if data.get('menu_date').date() == localtime().date() and localtime().hour >= 10:
                raise forms.ValidationError("The menu with today's date can be entered until 10:00 AM")
            if data.get('menu_date') < localtime():
                raise forms.ValidationError("The menu date cannot be less than today's date")


class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['starter', 'main_course', 'desserts', 'menu_date']
        widgets = {
            'menu_date': forms.TextInput(attrs={'type': 'date', 'required': 'true'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu', 'customization']
        widgets = {
            'menu': forms.Select(),
            'customization': forms.Textarea(),
        }

    def clean(self):
        if localtime().hour >= 11:
            raise forms.ValidationError("The menu can be ordered until 11:00 AM.")


class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu', 'customization']

        widgets = {
            'menu': forms.Select(),
            'customization': forms.Textarea(),
        }
