from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user manager for the CustomUser model.
    """

    def create_user(self, email, password, **args):
        """
        Creates a new user with the given email and password.
        """
        if not email:
            raise ValueError("Email is not provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **args)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **args):
        """
        Creates a new superuser with the given email and password.
        """
        args.setdefault("is_staff", True)
        args.setdefault("is_superuser", True)
        args.setdefault("is_active", True)
        if not email:
            raise ValueError("Email is not provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **args)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser.
    """

    # Removing the username field and replacing it with email
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # Adding custom fields for staff and superuser status
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Overriding the is_active field
    is_active = models.BooleanField(default=True)

    # Using email as the USERNAME_FIELD
    USERNAME_FIELD = "email"

    # No additional required fields
    REQUIRED_FIELDS = []

    # Using the custom UserManager for managing users
    objects = UserManager()
