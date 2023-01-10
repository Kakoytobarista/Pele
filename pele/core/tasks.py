import os
from datetime import datetime

from celery import shared_task
import logging

from django.db.models import Q

from appointment.utils import send_mail_custom
from appointment.models import Appointment
from pele.settings import BASE_DIR

logger = logging.getLogger(__name__)


@shared_task
def notify_appointment():
    """
    task job for notify client
    about appointment today
    :return: None
    """
    current_date = datetime.now().date()
    appointments = Appointment.objects.filter(~Q(email=""),
                                              is_available=False)
    for appointment in appointments:
        date = datetime.strptime(f'{appointment.date}', '%Y-%m-%d').date()
        if date == current_date:
            logger.debug('Send notification to user: '
                         f'{appointment.name} - {appointment.email}')
            send_mail_custom(name=appointment.name,
                             date=appointment.date,
                             time=appointment.time_begin,
                             email=appointment.email,
                             mail_subject='Notification about today visit')


@shared_task
def remove_unusable_appointment_job():
    """
    Cron for delete unusable appointment
    that don't used before current time
    """
    current_date = datetime.now().date()
    appointments = Appointment.objects.filter(name="",
                                              is_available=True,
                                              date__lt=current_date)
    if len(appointments) > 1:
        for appointment in appointments:
            logger.debug(appointment)
            appointment.delete()


@shared_task
def clean_log_file_job():
    """
    Cron job for cleaning log file 'django.log'
    :return: None
    """
    path_to_logs = str(BASE_DIR) + '/logs/django.log'
    logger.debug('Delete log file')
    os.remove(path_to_logs)


@shared_task
def test_task():
    send_mail_custom(name="hey",
                     date=datetime.now(),
                     time=datetime.now(),
                     email="HeyDevAslan@gmail.com",
                     mail_subject='Notification about today visit')
