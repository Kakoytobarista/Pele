from rest_framework.viewsets import mixins, GenericViewSet


class AppointmentMixinViewSet(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              GenericViewSet):
    pass
