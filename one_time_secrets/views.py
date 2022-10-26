from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Secret
from .serializers import SecretSerializer


class SecretCreateView(generics.CreateAPIView):
    serializer_class = SecretSerializer

    def post(self, request):
        secret_new = Secret.objects.create(
            text = request.data['text'],
            secret_word = request.data['secret_word']
        )
        secret_new = model_to_dict(secret_new)
        print(secret_new)
        return Response({'access_uid': secret_new['access_uid']})
