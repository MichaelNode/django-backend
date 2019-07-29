from django.contrib import messages
from django.utils.timezone import localtime
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .forms import GenerateNotificationUserForm
from .task import generate_notification


class GenerateSendNotification(FormView):
    template_name = 'notification/send_notification.html'
    form_class = GenerateNotificationUserForm

    def form_valid(self, form):
        if localtime().hour >= 18:
            messages.warning(
                self.request,
                '"Notifications can be sent until 11:00 AM.'
            )
            return redirect('home')
        else:
            generate_notification.delay()
            messages.success(
                self.request,
                'We are sending the notifications to employees.'
            )
            return redirect('home')
