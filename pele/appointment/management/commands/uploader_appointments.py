from datetime import datetime, timedelta

from django.core.management import BaseCommand

from appointment.models import Appointment


class UploadAppointmentsObject(BaseCommand):
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

    def add_arguments(self, parser):
        parser.add_argument('arg', type=int)

    def handle(self, *args, **options):
        num = options['arg']
        start_time_weekdays = datetime.strptime(f'{args} 9:00AM', '%Y-%m-%d %I:%M%p').time()
        end_time_weekdays = datetime.strptime(f'{args} 8:00PM', '%Y-%m-%d %I:%M%p').time()

        start_time_saturday = datetime.strptime(f'{args} 10:00AM', '%Y-%m-%d %I:%M%p').time()
        end_time_saturday = datetime.strptime(f'{args} 3:00PM', '%Y-%m-%d %I:%M%p').time()

        date_start = datetime.strptime(f'{args} 9:00AM', '%Y-%m-%d %I:%M%p')
        start_count = 0

        while start_count < num:
            if date_start.strftime("%A") in self.WEEKDAYS:
                if date_start.time() > end_time_weekdays:
                    date_start += timedelta(days=1)
                    if date_start.strftime("%A") in self.WEEKDAYS:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_weekdays)
                    else:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_saturday)
                else:
                    print("Create Object")
                    Appointment.objects.create(date=date_start,
                                               time_begin=date_start.time(),
                                               time_end=(date_start + timedelta(minutes=60)).time())
                    Appointment.objects.create(date=date_start,
                                               time_begin=date_start.time(),
                                               time_end=(date_start + timedelta(minutes=60)).time())
                    print(date_start.strftime("%A"))
                    print(date_start.time())
                    print("_______________")
                    date_start += timedelta(minutes=60)

            if date_start.strftime("%A") in self.SATURDAY:
                if date_start.time() > end_time_saturday:
                    date_start += timedelta(days=2)
                    if date_start.strftime("%A") == self.SATURDAY:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_weekdays)
                    else:
                        print("Change day")
                        date_start = date_start.combine(date_start, start_time_weekdays)

                else:
                    Appointment.objects.create(date=date_start,
                                               time_begin=date_start.time(),
                                               time_end=(date_start + timedelta(minutes=60)).time())
                    Appointment.objects.create(date=date_start,
                                               time_begin=date_start.time(),
                                               time_end=(date_start + timedelta(minutes=60)).time())

                    print("Create Object")
                    print(date_start.strftime("%A"))
                    print(date_start.time())
                    print("_______________")
                    date_start += timedelta(minutes=60)
            start_count += 1


uploader = UploadAppointmentsObject()
uploader.handle("2022-10-31", 14)
