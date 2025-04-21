from django.db import models
from users.models import CustomUser

# Employment status choices


class UserProfile(models.Model):
    # Linking the profile to the custom user model
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # Fields for the profile
    first_name = models.CharField(max_length=100, blank=True, null=True, help_text="User's first name")
    last_name = models.CharField(max_length=100, blank=True, null=True, help_text="User's last name")
    username_description = models.TextField(blank=True, null=True, help_text="A short description about the user")
    cv = models.FileField(upload_to='cv/', blank=True, null=True, help_text="User's CV in PDF format")
    languages = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated list of languages")
    
    
    # User's current job or unemployment description
    current_job = models.CharField(
        max_length=255, blank=True, null=True, help_text="Current job title or description of unemployment status"
    )

   

    def __str__(self):
        return f"{self.user.username}'s Profile"
