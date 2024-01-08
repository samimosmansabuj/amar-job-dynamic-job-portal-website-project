from django.urls import path
from .views import *

urlpatterns = [
    path('sign-in/', signin, name='signin'),
    path('sign-out/', signout, name='signout'),
    path('sign-up/', signup, name='signup'),
]