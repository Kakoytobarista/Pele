from django.contrib import admin

from appointment.models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    last_display = (
        'date',
        'time_begin',
        'time_end',
        'is_available'
    )


admin.site.register(Appointment, AppointmentAdmin)
