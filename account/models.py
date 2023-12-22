from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Custom_User(AbstractUser):
    USER_TYPE = (
        ('Recruiter', 'Recruiter'),
        ('JobSeeker', 'JobSeeker'),
        ('Employee', 'Employee'),
        ('Administrator', 'Administrator'),
        ('Admin', 'Admin'),
    )
    
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPE, blank=True, null=True)
    
    auth_token = models.CharField(max_length=500, blank=True, null=True)
    otp_token = models.CharField(max_length=6, blank=True, null=True)
    is_varified = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.username
    



