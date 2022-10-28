from rest_framework import serializers
from .models import Secret


class SecretCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secret
        fields = ('text', 'secret_word', 'access_uid', 'time_of_death', 'time_system')
        
    
    def create(self, validated_data):
        return Secret.objects.create(**validated_data)


class SecretGiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secret
        fields = ('text', 'secret_word')
        read_only_fields = ['text']