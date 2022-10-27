from datetime import datetime, timedelta

from appointment.models import Appointment


class UploadAppointmentsObject:
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

    def upload_data_to_db_original(self, date, appointments_count):
        start_time_weekdays = datetime.strptime(f'{date} 9:00AM', '%Y-%m-%d %I:%M%p').time()
        end_time_weekdays = datetime.strptime(f'{date} 8:00PM', '%Y-%m-%d %I:%M%p').time()

        start_time_saturday = datetime.strptime(f'{date} 10:00AM', '%Y-%m-%d %I:%M%p').time()
        end_time_saturday = datetime.strptime(f'{date} 3:00PM', '%Y-%m-%d %I:%M%p').time()

        date_start = datetime.strptime(f'{date} 9:00AM', '%Y-%m-%d %I:%M%p')
        start_count = 0

        while start_count < appointments_count:
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
                    Appointment.objects.create()
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
                    print("Create Object")
                    print(date_start.strftime("%A"))
                    print(date_start.time())
                    print("_______________")
                    date_start += timedelta(minutes=60)
            start_count += 1


uploader = UploadAppointmentsObject()
uploader.upload_data_to_db_original("2022-10-31", 14)
