from django.urls import path
from . import views


urlpatterns = [
    path('generate/', views.SecretCreateView.as_view()),
    path('secrets/<uuid:access_uid>/', views.give_secret_view),
]
