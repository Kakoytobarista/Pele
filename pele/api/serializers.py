from rest_framework import serializers

from appointment.models import Appointment


class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields


class AppointmentCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for model Appointment. This serializer
    work for getting data.
    """
    class Meta:
        model = Appointment
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'date',
            'time_begin',
            'time_end',
        )
        read_only_fields = ('date',
                            'time_begin',
                            'time_end',
                            )


class AppointmentSerializer(ReadOnlyModelSerializer):
    """
    Serializer for model Appointment. This serializer work
    for creating data.
    """
    class Meta:
        model = Appointment
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'date',
            'time_begin',
            'time_end',
            'is_available',
            'comment',
        )
