from django.contrib import admin
from .models import Secret


@admin.register(Secret)
class SecretAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('text', 'secret_word', 'access_uid')
        }),
        (None, {
            'fields': (('time_of_death', 'time_system'),)
        }),
    )
