from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import BaseManager

# Create your models here.
class Custom_User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('Recruiter', 'Recruiter'),
        ('JobSeeker', 'JobSeeker'),
        ('Employee', 'Employee'),
        ('Administrator', 'Administrator'),
        ('Admin', 'Admin'),
    )
    username = models.CharField(max_length=100, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(max_length=200)
    user_type = models.CharField(max_length=100, choices=USER_TYPE, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    auth_token = models.CharField(max_length=500, blank=True, null=True)
    otp_token = models.CharField(max_length=6, blank=True, null=True)
    is_varified = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    objects = BaseManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self) -> str:
        return self.username


class Recruiter(Custom_User):
    comapany_name = models.CharField(max_length=100)
    comapany_phone_number = models.CharField(max_length=100)
    company_address = models.CharField(max_length=500, blank=True, null=True)
    company_logo = models.ImageField(upload_to='company/logo/', blank=True, null=True)
    comapany_details = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username

class JobSeeker(Custom_User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    profile_picture = models.ImageField(upload_to='jobseeker/profile_picture/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, blank=True, null=True, max_length=20)
    short_details = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username

