from datetime import datetime, timedelta
import logging

from django.core.management.base import BaseCommand

from appointment.models import Appointment
from appointment.utils import create_two_appointment_objects
from users.models import User


logger = logging.getLogger(__name__)


def myIter(seq: list):
    """
    You can use 2 loop
    :param seq:
    :return:
    """
    count = 0
    while True:
        if count == len(seq):
            count = 0
        else:
            yield seq[count]
            count += 1


def barber_generator(barbers):
    while True:
        for w in barbers:
            yield w


class Command(BaseCommand):
    """
    Function for uploading appointments to
    db.
    :param appointments_cont:
    :param date: date from we will create appointments
    :return:
    """
    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", ]
    SATURDAY = "Saturday"
    SUNDAY = "Closed"
    BARBER_GEN = barber_generator(User.objects.filter(role="barber_user"))

    def add_arguments(self, parser):
        parser.add_argument('date_start', type=str)
        parser.add_argument('date_end', type=str)

    def handle(self, *args, **options):
        date_start_str = options['date_start']
        date_end_str = options['date_end']
        start_time_weekdays = datetime.strptime(f'{date_start_str} 9:00AM', '%Y-%m-%d %I:%M%p').time()
        end_time_weekdays = datetime.strptime(f'{date_start_str} 8:00PM', '%Y-%m-%d %I:%M%p').time()

        start_time_saturday = datetime.strptime(f'{date_start_str} 10:00AM', '%Y-%m-%d %I:%M%p').time()
        end_time_saturday = datetime.strptime(f'{date_start_str} 4:00PM', '%Y-%m-%d %I:%M%p').time()

        date_start = datetime.strptime(f'{date_start_str} 9:00AM', '%Y-%m-%d %I:%M%p')
        date_end = datetime.strptime(f'{date_end_str} 9:00AM', '%Y-%m-%d %I:%M%p')

        if datetime.now() > date_start:
            return None

        while date_start < date_end:
            if date_start.strftime("%A") in self.WEEKDAYS:
                if date_start.time() >= end_time_weekdays:
                    date_start += timedelta(days=1)
                    if date_start.strftime("%A") in self.WEEKDAYS:
                        date_start = date_start.combine(date_start, start_time_weekdays)
                    else:
                        logger.debug(f'Change day to {date_start.date()}')
                        date_start = date_start.combine(date_start, start_time_saturday)
                else:
                    create_two_appointment_objects(appointment_object=Appointment,
                                                   date=date_start,
                                                   barber_gen=self.BARBER_GEN)
                    logger.debug(f'Created Objects {date_start.strftime("%A")} - {date_start}')
                    date_start += timedelta(minutes=30)

            if date_start.strftime("%A") == self.SATURDAY:
                if date_start.time() >= end_time_saturday:
                    date_start += timedelta(days=2)
                    if date_start.strftime("%A") == self.SATURDAY:
                        logger.debug(f'Change day to {date_start.date()}')
                        date_start = date_start.combine(date_start, start_time_weekdays)
                    else:
                        date_start = date_start.combine(date_start, start_time_weekdays)
                        logger.debug(f'Change day to {date_start.date()}')

                else:
                    create_two_appointment_objects(appointment_object=Appointment,
                                                   date=date_start,
                                                   barber_gen=self.BARBER_GEN)
                    logger.debug(f'Created Objects {date_start.strftime("%A")} - {date_start}')
                    date_start += timedelta(minutes=30)
