from django.contrib import admin
from .models import Custom_User, Recruiter, JobSeeker

# Register your models here.
@admin.register(Custom_User)
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['username','email', 'user_type', 'is_varified']

@admin.register(Recruiter)
class Recruiter_Admin(admin.ModelAdmin):
    list_display = ['username', 'comapany_name', 'email', 'comapany_phone_number', 'user_type', 'is_varified']

@admin.register(JobSeeker)
class JobSeeker_Admin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'phone_number', 'user_type', 'is_varified']
