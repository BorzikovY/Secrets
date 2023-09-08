from rest_framework import serializers
from .models import Secret


class SecretCreateSerializer(serializers.ModelSerializer):
    '''Secret create serializer'''

    class Meta:
        model = Secret
        fields = ('text', 'secret_word', 'access_uid', 'time_of_death', 'time_system')
        
    
    def create(self, validated_data) -> Secret:
        return Secret.objects.create(**validated_data)
