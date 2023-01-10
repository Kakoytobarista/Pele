import logging
from datetime import datetime, timedelta
from typing import Generator

from django.core.mail import send_mail
from django.template.loader import get_template
from pele import settings

logger = logging.getLogger(__name__)


def convert_to_day_month_year(date: datetime):
    """
    Function for convert string to datetime
    :param date: datetime object
    :return: datetime object
    """
    date = datetime.strptime(f'{date}', '%Y-%m-%d')
    reformat = "{}-{}-{}".format(date.day,
                                 date.month,
                                 date.year)
    return reformat


def send_mail_custom(name: str, date: datetime,
                     time: datetime, email: str,
                     mail_subject: str = 'You have successfully booked an appointment to haircut!'):
    """
    Function for send email for confirmation email address.
    """
    context = {
        'name': name,
        'date': convert_to_day_month_year(date),
        'time': time
    }
    send_mail(mail_subject, name, settings.EMAIL_HOST_USER,
              [email], fail_silently=True,
              html_message=get_template('email_letter.html').render(context))

def time_in_range(array_with_intervals: list, current_start: datetime.time,
                  current_end: datetime.time):
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


def create_two_appointment_objects(appointment_object,
                                   date: datetime,
                                   barber_gen: Generator):
    """
    Function for creating appointments (create objects
    of appoitnments and save into data base)
    :param appointment_object: Appointment object
    :param date: datetime object
    :param barber_gen: generator object
    :return: None
    """
    for i in range(3):
        appointment_object.objects.create(date=date,
                                          time_begin=date.time(),
                                          time_end=(date + timedelta(minutes=30)).time(),
                                          barber=barber_gen.__next__())
