from datetime import datetime

from appointment.models import Appointment


def get_queryset_for_available_appointment(data: dict,
                                           appointment_obj: Appointment()):
    """
    Function for getting actual available appointments
    with time not less with current and desired barber
    :param data: data from request
    :param appointment_obj: objects of class Appointment
    :return: queryset
    """
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    date_db = datetime.strptime(data.get('date'), '%Y-%m-%d').date()
    if current_date > date_db:
        return None

    elif current_date == date_db:
        queryset = appointment_obj.objects.filter(date=date_db,
                                                  time_begin__gt=current_time,
                                                  is_available=True, barber=data.get('barber'))

    else:
        queryset = appointment_obj.objects.filter(date=date_db,
                                                  is_available=True,
                                                  barber=data.get('barber'))

    return queryset
