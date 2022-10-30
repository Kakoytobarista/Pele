from datetime import timedelta

from django.core.mail import send_mail
from django.template.loader import get_template

from pele import settings


def send_mail_custom(request, data):
    """
    Function for send email for confirmation email address.
    """

    mail_subject = 'You have successfully booked an appointment to haircut!'
    context = {
        'name': data["name"],
        'date': request.session["date"],
        'time': request.session["time"]
    }
    send_mail(mail_subject, data["name"], settings.EMAIL_HOST_USER, [data["email"]], fail_silently=False,
              html_message=get_template("email_letter.html").render(context))


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


def create_two_appointment_objects(appointment_object,
                                   date,
                                   barber_gen):
    appointment_object.objects.create(date=date,
                                      time_begin=date.time(),
                                      time_end=(date + timedelta(minutes=60)).time(),
                                      barber=barber_gen.__next__())
    appointment_object.objects.create(date=date,
                                      time_begin=date.time(),
                                      time_end=(date + timedelta(minutes=60)).time(),
                                      barber=barber_gen.__next__())
