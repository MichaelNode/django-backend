from django import forms
from main.models import Menu, Order
from django.utils.timezone import localtime


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['starter', 'main_course', 'desserts', 'menu_date']
        widgets = {
            'menu_date': forms.TextInput(
                attrs={
                    'type': 'date',
                    'required': 'true'
                }),
        }

    def clean(self):
        data = self.cleaned_data
        if data.get('menu_date'):
            # validate that menu is created before 10:00 AM
            if data.get('menu_date').date() == localtime().date() \
                    and localtime().hour >= 10:
                raise forms.ValidationError(
                    "The menu with today's date can be entered until 10:00 AM"
                )
            if data.get('menu_date') < localtime():
                raise forms.ValidationError(
                    "The menu date cannot be less than today's date"
                )


class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['starter', 'main_course', 'desserts', 'menu_date']
        widgets = {
            'menu_date': forms.TextInput(
                attrs={
                    'type': 'date',
                    'required': 'true'
                }),
        }

    def clean(self):
        data = self.cleaned_data
        if data.get('menu_date'):
            # validate that the menu is edited until 10:00 AM
            if data.get('menu_date').date() == localtime().date() \
                    and localtime().hour >= 10:
                raise forms.ValidationError(
                    "The menu with today's date can be entered until 10:00 AM"
                )
            if data.get('menu_date') < localtime():
                raise forms.ValidationError(
                    "The menu date cannot be less than today's date"
                )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu', 'customization']
        widgets = {
            'menu': forms.Select(),
            'customization': forms.Textarea(),
        }

    # Validate that employees can only order the menu until 11:00 am
    def clean(self):
        if localtime().hour >= 11:
            raise forms.ValidationError(
                "The menu can be ordered until 11:00 AM."
            )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # load the menu list of the current day
        self.fields['menu'].queryset = \
            Menu.objects.filter(
            menu_date=localtime().date()
        )


class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu', 'customization']
        widgets = {
            'menu': forms.Select(),
            'customization': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(OrderEditForm, self).__init__(*args, **kwargs)
        # load the menu list of the current day
        self.fields['menu'].queryset = \
            Menu.objects.filter(
                menu_date=localtime().date()
            )

    # Validate that employees can only order the menu until 11:00 am
    def clean(self):
        if localtime().hour >= 11:
            raise forms.ValidationError(
                "The order with today's date can be edited until 11:00 AM."
            )
