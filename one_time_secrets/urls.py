
from django.urls import path
from .views import index

urlpatterns = [
    path('generate/', index),
    path('secrets/key/', index),
]