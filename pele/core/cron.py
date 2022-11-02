from datetime import datetime

from django.db.models import Q

from appointment.models import Appointment
from appointment.utils import send_mail_custom


def notification_job():
    current_date = datetime.now().date()
    appointments = Appointment.objects.filter(~Q(email=""), is_available=False)
    for appointment in appointments:
        date = datetime.strptime(f'{appointment.date}', '%Y-%m-%d').date()
        if date == current_date:
            send_mail_custom(name=appointment.name,
                             date=appointment.date,
                             time=appointment.time_begin,
                             email=appointment.email,
                             mail_subject="Notification about today visit")


def remove_unusable_appointment():
    """Cron for delete unusable appointment
    that don't used before current time"""
    current_date = datetime.now().date()
    appointments = Appointment.objects.filter(name="",
                                              is_available=True,
                                              date__lt=current_date)
    if len(appointments) > 1:
        for i in appointments:
            i.delete()
