from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Fields from the registration form
    email = models.EmailField(unique=True)  # Email address
    first_name = models.CharField(max_length=150)  # Name
    password1 = models.CharField(max_length=128)  # Password (hashed)
    password2 = models.CharField(max_length=128)  # Password confirmation (hashed)
    contact_number = models.CharField(max_length=15)  # Contact Number

    # Add any other custom fields you need

    def __str__(self):
        return self.username
