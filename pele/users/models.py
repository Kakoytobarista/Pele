from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    AUTH_USER = 'auth_user'
    ADMIN_USER = 'admin'
    BARBER_USER = 'barber_user'
    ROLE_VERBOSE_NAME = 'User role'
    USER_ROLE_CHOICES = [
        (AUTH_USER, 'Auth user'),
        (ADMIN_USER, 'Admin user'),
        (BARBER_USER, 'Barber user')
    ]
    role = models.TextField(
        choices=USER_ROLE_CHOICES,
        default=AUTH_USER,
        verbose_name=ROLE_VERBOSE_NAME,
    )
    phone = models.CharField(
        verbose_name='Phone number',
        help_text='Phone number for user',
        max_length=50
    )
    work_experience = models.IntegerField(verbose_name='Work of experience as '
                                                       'barber',
                                          help_text='Field for setting how much '
                                                    'barber have',
                                          blank=True,
                                          null=True,
                                          unique=False)
