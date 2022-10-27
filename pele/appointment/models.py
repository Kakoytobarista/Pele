from django.db import models
from rest_framework.exceptions import ValidationError

from appointment.utils import time_in_range
from users.models import User


class Appointment(models.Model):
    name = models.CharField(verbose_name='First name and Second name',
                            max_length=100,
                            help_text='Field for setting First '
                                      'name and Second name',
                            blank=True)
    email = models.EmailField(verbose_name='Email address',
                              help_text='Field for getting email address '
                                        'from client',
                              blank=True)
    phone = models.CharField(verbose_name='Phone number',
                             help_text='Field for getting phone number of the'
                                       'client',
                             max_length=100,
                             blank=True)
    date = models.DateField(verbose_name='Date of appointment',
                            help_text='Field for setting date of appointment')
    time_begin = models.TimeField(verbose_name='Start of the appointment',
                                  help_text='Field for setting start of the appointment')
    time_end = models.TimeField(verbose_name='End of the appointment',
                                help_text='Field for setting end of the appointment')
    is_available = models.BooleanField(verbose_name='Is available of appointment',
                                       help_text='Field for setting status of the '
                                                 'appointment (available or not)',
                                       default=True)
    barber = models.ForeignKey(to=User,
                               on_delete=models.SET_NULL,
                               verbose_name='Barber of this appointment',
                               blank=True,
                               null=True)
    comment = models.CharField(verbose_name='Comments of the appointment',
                               max_length=300,
                               help_text='Field for setting comments about your'
                                         'haircut',
                               blank=True)

    def clean(self):
        intervals = []
        objects = Appointment.objects.filter(date=self.date,
                                             barber=self.barber)
        for i in objects:
            intervals.append((i.time_begin, i.time_end))
        if time_in_range(array_with_intervals=intervals,
                         current_start=self.time_begin, current_end=self.time_end):
            raise ValidationError({'time_end': 'End date cannot be smaller then start date.'})

    def __str__(self):
        return f"Appointment: {self.date}, {self.time_begin}-{self.time_end}"

    class Meta:
        ordering = ['-date']
        unique_together = (
            'date',
            'time_begin',
            'time_end',
            'barber',
        )
