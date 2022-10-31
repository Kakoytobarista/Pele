from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from appointment.models import Appointment
from appointment.utils import create_two_appointment_objects
from users.models import User


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
        end_time_saturday = datetime.strptime(f'{date_start_str} 3:00PM', '%Y-%m-%d %I:%M%p').time()

        date_start = datetime.strptime(f'{date_start_str} 9:00AM', '%Y-%m-%d %I:%M%p')
        date_end = datetime.strptime(f'{date_end_str} 9:00AM', '%Y-%m-%d %I:%M%p')

        while date_start < date_end:
            if date_start.strftime("%A") in self.WEEKDAYS:
                if date_start.time() >= end_time_weekdays:
                    date_start += timedelta(days=1)
                    if date_start.strftime("%A") in self.WEEKDAYS:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_weekdays)
                    else:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_saturday)
                else:
                    print(date_start)
                    print(date_start)
                    create_two_appointment_objects(appointment_object=Appointment,
                                                   date=date_start,
                                                   barber_gen=self.BARBER_GEN)
                    print("Created Objects")
                    print(date_start.strftime("%A"))
                    print(date_start.time())
                    print("_______________")
                    date_start += timedelta(minutes=30)

            if date_start.strftime("%A") in self.SATURDAY:
                if date_start.time() >= end_time_saturday:
                    date_start += timedelta(days=2)
                    if date_start.strftime("%A") == self.SATURDAY:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_weekdays)
                    else:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_weekdays)

                else:
                    create_two_appointment_objects(appointment_object=Appointment,
                                                   date=date_start,
                                                   barber_gen=self.BARBER_GEN)
                    print("Created Objects")
                    print(date_start.strftime("%A"))
                    print(date_start.time())
                    print("_______________")
                    date_start += timedelta(minutes=30)
