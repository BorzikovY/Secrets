from django.contrib import admin
from .models import Secret


@admin.register(Secret)
class SecretAdmin(admin.ModelAdmin):
    fields = ['text', 'secret_word', 'access_uid']

