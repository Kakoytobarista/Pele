from django.urls import include, path
from rest_framework import routers


from api.views import AppointmentViewSet, UserViewSet

app_name = 'api'


router = routers.DefaultRouter()
router.register('appointments', AppointmentViewSet, basename='appointment')
router.register('users', UserViewSet, basename='users')

urlpatterns = (
    path('', include(router.urls)),
)
