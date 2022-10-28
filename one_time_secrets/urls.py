from django.urls import path
from .views import SecretCreateView, SecretGiveView


urlpatterns = [
    path('generate/', SecretCreateView.as_view()),
    path('secrets/<uuid:access_uid>', SecretGiveView.as_view()),
]
