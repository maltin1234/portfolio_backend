from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager  # Import the custom manager
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Make email unique
    description = models.TextField(max_length=500, blank=True)
    linkedin_url = models.TextField(max_length=500, blank=True)

    # first_name and last_name are already part of AbstractUser, no need to redefine them

    # Use email as the unique identifier for authentication, but keep username
    USERNAME_FIELD = 'email'  # Email will be used as the login field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Username, first name, and last name are still required
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email  # Or use self.username if you prefer
    
class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveIntegerField()  # Ensure the rating is positive
    feedback = models.TextField(blank=True, null=True)  # Optional feedback
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the rating was created
    class Meta:
        unique_together = ('user', 'created_at')  # Ensure no duplicate ratings at the same time
        ordering = ['-created_at']  # Sort by newest ratings first
    def __str__(self):
        return f"{self.user.email} - {self.rating}"