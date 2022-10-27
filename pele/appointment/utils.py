from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpRequest

from pele import settings


def send_mail_custom(request: HttpRequest, data):
    """
    Function for send email for confirmation enail address.
    """

    current_site = get_current_site(request)
    mail_subject = 'Activate your blog account.'
    message = f"Hello man {data['name']}, {current_site}"
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [data["email"]], fail_silently=False)


def time_in_range(array_with_intervals, current_start, current_end):
    """
    Returns whether current is in the range [start, end]
    """
    result = []
    for begin, end in array_with_intervals:
        if (begin < current_start < end) or (begin < current_end < end):
            result.append(True)
        else:
            result.append(False)

    if any(result):
        return True
    return False
