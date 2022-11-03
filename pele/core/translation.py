from modeltranslation.translator import register, TranslationOptions
from appointment.models import Appointment
from users.models import User


@register(Appointment)
class AppointmentTranslationOptions(TranslationOptions):
    pass


@register(User)
class UserTranslationOptions(TranslationOptions):
    pass
