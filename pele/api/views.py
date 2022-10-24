from datetime import datetime

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.mixins import AppointmentMixinViewSet
from api.utils import get_queryset_for_available_appointment
from appointment.models import Appointment
from api.serializers import AppointmentSerializer, AppointmentCreateSerializer


class AppointmentViewSet(AppointmentMixinViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ('date', 'is_available')
    http_method_names = ['get', 'patch',
                         'delete', 'post', ]

    def get_serializer_class(self):
        if self.request.method in ('put',
                                   'patch',
                                   'delete', ):
            return AppointmentCreateSerializer

        return AppointmentSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        Partial update appointment object
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        appointment_object = get_object_or_404(Appointment, id=kwargs['pk'])
        data = request.data
        appointment_object.name = data.get('name', appointment_object.name)
        appointment_object.email = data.get('email', appointment_object.email)
        appointment_object.phone = data.get('phone', appointment_object.phone)
        appointment_object.comment = data.get('comment', appointment_object.comment)
        appointment_object.is_available = False
        appointment_object.save()
        serializer = AppointmentCreateSerializer(appointment_object)
        return Response(serializer.data, status.HTTP_206_PARTIAL_CONTENT)

    @action(methods=('post',), detail=False)
    def get_available_appointment_on_current_day(self, request):
        data = request.data
        queryset = get_queryset_for_available_appointment(data=data,
                                                          appointment_obj=Appointment)
        serializer = AppointmentSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
