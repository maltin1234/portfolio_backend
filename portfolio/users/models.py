from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    description = models.TextField(max_length=500, blank=True)
    linkedin_url = models.TextField(max_length=500, blank=True)

    USERNAME_FIELD = 'email'  # Use email as the unique identifier for authentication
    REQUIRED_FIELDS = ['username']  # List fields that are required when creating a user

    def __str__(self):
        return self.email  # Or username if preferred
