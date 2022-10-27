from django.contrib import admin


from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'barber_first_name',
        'barber_second_name',
        'work_experience',
    )
    fields = (
        'username',
        'barber_first_name',
        'barber_second_name',
        'work_experience',
    )

