from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Secret
from .serializers import SecretCreateSerializer, SecretGiveSerializer
from rest_framework import status
from .renderers import BaseJSONRenderer


class SecretCreateView(APIView):

    serializer_class = SecretCreateSerializer
    renderer_classes = (BaseJSONRenderer,)

    def post(self, request):
        print(request.data)
        time_of_death = int(request.data['time_of_death'])

        if time_of_death < 1 or time_of_death > 60:
            return Response({'message': 'time_of_death must be > 1 and < 60'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'access_uid': serializer.data['access_uid']}, status=status.HTTP_201_CREATED)


class SecretGiveView(generics.CreateAPIView):
    model = Secret
    serializers = SecretGiveSerializer

