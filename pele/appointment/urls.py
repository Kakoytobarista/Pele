from django.urls import path

from appointment import views

app_name = 'appointment'


urlpatterns = [
    path('appointment/', views.index, name='index')
]
