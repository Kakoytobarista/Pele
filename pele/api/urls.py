from django.urls import include, path
from rest_framework import routers


from api.views import AppointmentViewSet

app_name = 'api'


router = routers.DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointment')

urlpatterns = (
    path('', include(router.urls)),
)
