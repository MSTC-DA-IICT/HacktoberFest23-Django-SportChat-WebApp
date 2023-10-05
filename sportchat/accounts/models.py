from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # Add custom fields here
    Name = models.CharField(max_length=200,blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)

    # Add any other custom fields you need

    def __str__(self):
        return self.username


