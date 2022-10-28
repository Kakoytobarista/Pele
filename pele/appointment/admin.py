from django.contrib import admin

from appointment.models import Appointment


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
