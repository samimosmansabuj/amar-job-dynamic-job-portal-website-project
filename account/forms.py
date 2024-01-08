from django import forms
from .models import Custom_User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number', 'user_type', 'password']
        widgets = {
            "first_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter First Name'
            }),
            
            "last_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
            }),
            
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
            }),
            
            "username": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username'
            }),
            
            "phone_number": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number'
            }),
            
            "user_type": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select User Type'
            }),
            
            "password": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            })
        }