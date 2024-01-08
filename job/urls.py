from django.urls import path
from .views import *

urlpatterns = [
    path('job/', all_job, name='all_job'),
    path('job_details/', job_details, name='job_details'),
]