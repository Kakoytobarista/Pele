from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    phone = PhoneNumberField(verbose_name='Phone number',
                             help_text='Field for getting phone number of the'
                                       'client',
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
    comment = models.CharField(verbose_name='Comments of the appointment',
                               max_length=300,
                               help_text='Field for setting comments about your'
                                         'haircut',
                               blank=True)

    def __str__(self):
        return f"Appointment: {self.date}, {self.time_begin}-{self.time_end}"

    class Meta:
        ordering = ['-date']
