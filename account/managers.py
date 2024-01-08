from django.contrib.auth.base_user import BaseUserManager


class BaseManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username=username, password=password, email=email, **extra_fields)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.is_varified = True
        user.save()
        return user
