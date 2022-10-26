from django.db import models
from datetime import datetime
from .backends import generate_access_code


class Secret(models.Model):
    text = models.TextField()
    secret_word = models.CharField(max_length=16)
    access_code = models.CharField(max_length=30, default=generate_access_code())
    # date_of_creation = models.DateTimeField(auto_now_add=True, null=True)
    date_of_death = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)