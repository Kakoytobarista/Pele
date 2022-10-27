from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    barber_first_name = models.CharField(verbose_name='First name of the barber',
                                         help_text='Field for setting first name of the barber',
                                         max_length=50,
                                         blank=False)
    barber_second_name = models.CharField(verbose_name='Second Name of the barber',
                                          help_text='Field for setting second name '
                                                    'of the barber',
                                          max_length=50,
                                          blank=False,
                                          null=True)

    work_experience = models.IntegerField(verbose_name='Work of experience as '
                                                       'barber',
                                          help_text='Field for setting how much '
                                                    'barber have',
                                          blank=True,
                                          null=True,
                                          unique=False)
