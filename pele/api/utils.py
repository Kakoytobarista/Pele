from datetime import datetime


def get_queryset_for_available_appointment(data, appointment_obj):
    current_time = datetime.now().time()
    current_date = datetime.now().date().strftime('%Y-%m-%d')
    if current_date == data.get('date'):
        queryset = appointment_obj.objects.filter(date=data.get('date'),
                                                  time_end__gte=current_time,
                                                  is_available=True)
    else:
        queryset = appointment_obj.objects.filter(date=data.get('date'),
                                                  is_available=True)

    return queryset
