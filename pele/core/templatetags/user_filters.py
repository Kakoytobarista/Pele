from django import template
from django.utils.translation import gettext

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def add_id(field, css):
    return field.as_widget(attrs={'id': css})


@register.filter(name='translate')
def translate(text):
    try:
        return gettext(text)
    except:
        pass
