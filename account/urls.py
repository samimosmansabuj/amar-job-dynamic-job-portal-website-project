from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', registration, name='registration')
]