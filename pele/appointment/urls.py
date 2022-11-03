from django.urls import path


from appointment import views


app_name = 'appointment'


urlpatterns = [
    path('', views.index, name='index'),
    path('appointment_success/', views.success_appointment, name='success_appointment'),
]
