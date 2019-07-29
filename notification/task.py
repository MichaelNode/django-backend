import datetime
from django.http import Http404
from user.models import MyUser
from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def generate_notification():
    try:
        url = 'http://127.0.0.1:8000/today_menu'
        subject = 'Menu reminder ' + str(datetime.datetime.now().date())
        message = 'You can see the menu options for today in ' \
                  'the following link: ' \
                  + url + ' remember that you can only order until 11:00 AM '
        for user in MyUser.objects.exclude(email__isnull=True):
            email = EmailMessage(subject, message, to=[user.email, ])
            email.send()
        print('send email 1....')
    except MyUser.DoesNotExist:
        raise Http404("There are no employees")
    return 'ok'
