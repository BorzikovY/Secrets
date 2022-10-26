from django.db import models


class Secret(models.Model):
    text = models.CharField(max_length=254, blank=True, null=True)
    secret_word = models.CharField(max_length=60, blank=True, null=True)
    access_uid = models.UUIDField(blank=True, null=True)
    # date_of_creation = models.DateTimeField(auto_now_add=True, null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def save(self, **kwargs):
        if not self.access_uid:
            import uuid
            import random
            self.access_uid = uuid.uuid1(random.randint(0, 281474976710655))
        super().save(**kwargs)
