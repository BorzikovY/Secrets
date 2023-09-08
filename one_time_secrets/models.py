from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Secret(models.Model):
    '''Secret model'''
    
    TIME_SYSTEM = (
        ('MINUTES', 'minutes'),
        ('HOURS', 'hours'),
        ('DAYS', 'days'),
    )

    text = models.CharField(
        max_length=254, 
        blank=True, 
        null=True
    )
    secret_word = models.CharField(
        max_length=60, 
        blank=True, 
        null=True
    )
    access_uid = models.UUIDField(
        blank=True, 
        null=True
    )
    time_of_death =  models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    time_system = models.CharField(
        choices=TIME_SYSTEM, 
        default='minutes', 
        blank=True, 
        max_length=7
    )

    def save(self, **kwargs):
        if not self.access_uid:
            import uuid
            import random
            self.access_uid = uuid.uuid1(random.randint(0, 281474976710655))

        match self.time_system:
            case 'DAYS':
                self.time_of_death = self.time_of_death * 1440
                self.time_system = 'MINUTES'
            case 'HOURS':
                self.time_of_death = self.time_of_death * 60
                self.time_system = 'MINUTES'
            case 'MINUTES':
                pass

        super().save(**kwargs)

    def __str__(self) -> str:
        return str(self.id)
