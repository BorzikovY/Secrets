from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Secret
from .serializers import SecretCreateSerializer
from rest_framework import status
from .renderers import BaseJSONRenderer
from django.shortcuts import get_object_or_404


class SecretCreateView(APIView):
    '''Secret create View'''
    serializer_class = SecretCreateSerializer
    renderer_classes = (BaseJSONRenderer,)

    def post(self, request) -> Response:
        time_of_death = int(request.data['time_of_death'])

        if time_of_death < 1 or time_of_death > 60:
            return Response({'message': 'time_of_death must be > 1 and < 60'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'access_uid': serializer.data['access_uid']}, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['POST'])
def give_secret_view(request, access_uid) -> Response:
    secret = get_object_or_404(Secret, access_uid=access_uid)
    if request.data['secret_word'] == secret.secret_word:
        Secret.objects.filter(id=secret.id).delete()
        return Response({'text': secret.text}, status=status.HTTP_202_ACCEPTED)
    return Response({'message': 'incorrect secret word'}, status=status.HTTP_403_FORBIDDEN)
