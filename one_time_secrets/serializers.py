from rest_framework import serializers
from .models import Secret


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ('text', 'secret_word', 'access_uid',)
        read_only_fields = ['access_uid']


