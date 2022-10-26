
from django.urls import path
from .views import SecretCreateView
# from .views import index

urlpatterns = [
    path('generate/', SecretCreateView.as_view()),
    # path('secrets/key', index),
]