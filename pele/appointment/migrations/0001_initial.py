# Generated by Django 4.1.2 on 2022-10-23 14:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Field for setting First name and Second name', max_length=100, verbose_name='First name and Second name')),
                ('email', models.EmailField(blank=True, help_text='Field for getting email address from client', max_length=254, verbose_name='Email address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('date', models.DateField(help_text='Field for setting date of appointment', verbose_name='Date of appointment')),
                ('time_begin', models.TimeField(help_text='Field for setting start of the appointment', verbose_name='Start of the appointment')),
                ('time_end', models.TimeField(help_text='Field for setting end of the appointment', verbose_name='End of the appointment')),
                ('is_available', models.BooleanField(default=True, help_text='Field for setting status of the appointment (available or not)', verbose_name='Is available of appointment')),
                ('comment', models.CharField(help_text='Field for setting comments about yourhaircut', max_length=300, verbose_name='Comments of the appointment')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
