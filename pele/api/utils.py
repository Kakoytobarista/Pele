from datetime import datetime


def get_queryset_for_available_appointment(data, appointment_obj):
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    date_db = datetime.strptime(data.get('date'), '%Y-%m-%d').date()
    if current_date > date_db:
        return None

    elif current_date == date_db:
        queryset = appointment_obj.objects.filter(date=date_db,
                                                  time_end__gte=current_time,
                                                  is_available=True)
    else:
        queryset = appointment_obj.objects.filter(date=date_db,
                                                  is_available=True)

    return queryset
