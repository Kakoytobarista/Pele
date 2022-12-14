# Generated by Django 4.1.2 on 2022-11-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['date']},
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='appointment',
            name='comment_en',
            field=models.CharField(blank=True, help_text='Field for setting comments about yourhaircut', max_length=300, null=True, verbose_name='Comments of the appointment'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='comment_sr',
            field=models.CharField(blank=True, help_text='Field for setting comments about yourhaircut', max_length=300, null=True, verbose_name='Comments of the appointment'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='name_en',
            field=models.CharField(blank=True, help_text='Field for setting First name and Second name', max_length=100, null=True, verbose_name='First name and Second name'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='name_sr',
            field=models.CharField(blank=True, help_text='Field for setting First name and Second name', max_length=100, null=True, verbose_name='First name and Second name'),
        ),
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.UniqueConstraint(fields=('date', 'time_begin', 'time_end', 'barber'), name='unique appointment'),
        ),
    ]
