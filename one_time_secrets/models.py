from django.db import models
from django.contrib.auth.models import BaseUserManager


class Secret(models.Model):
    text = models.TextField()
    secret_word = models.CharField(max_length=16)
    access_code = models.CharField(max_length=30, default=lambda: BaseUserManager().make_random_password(30), unique=True)
    # date_of_creation = models.DateTimeField(auto_now_add=True, null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
