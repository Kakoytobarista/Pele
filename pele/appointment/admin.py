from django.contrib import admin

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



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    date_hierarchy = "date"
    fields = (
        'name',
        'date',
        'email',
        'phone',
        'time_begin',
        'time_end',
        'is_available',
        'comment',
        'barber',
    )
    list_display = (
        "name",
        "date",
        "time_begin",
        "time_end",
        "is_available",
        'barber',
    )
    list_editable = (
        "name",
        "time_begin",
        "time_end",
        "is_available",
        'barber',
    )
    empty_value_display = "--- EMPTY ---"
    list_filter = (
        'is_available',
        'barber'
    )
    search_fields = (
        'date',
        'barber'
    )
    list_display_links = (
        'date',
    )
    admin.site.empty_value_display = '(None)'
