from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from users.models import User


@admin.register(User)
class UserAdmin(TranslationAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'role',
        'work_experience',
    )
    fields = (
        'username',
        'first_name',
        'last_name',
        'password',
        'email',
        'phone',
        'role',
        'work_experience',
        'is_active',
    )

