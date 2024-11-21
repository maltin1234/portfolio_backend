from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

class EmailBackend(ModelBackend):
    """
    Custom authentication backend that allows login with email.
    """
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        # If email is not provided, fallback for username (used in admin login)
        if not email:
            email = username  # Admin login passes 'username'

        if not email:
            raise AuthenticationFailed("Email is required.")

        try:
            # Get the user by email
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise AuthenticationFailed("No active account found with the given credentials.")

        # Check the password
        if user.check_password(password):
            return user
        else:
            raise AuthenticationFailed("Incorrect password.")
