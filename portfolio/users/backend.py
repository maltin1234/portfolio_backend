from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

class EmailBackend(ModelBackend):
    """
    Custom authentication backend that allows login with email.
    """
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Check if email is provided
        if not email:
            raise AuthenticationFailed("Email is required.")

        # Log the input username (which is expected to be the email)
        print(f"Attempting to authenticate user with email: {email}")

        try:
            # Assume `username` is actually the email
            user = UserModel.objects.get(email=email)
            print(f"User found: {user}")
        except UserModel.DoesNotExist:
            raise AuthenticationFailed("No active account found with the given credentials.")

        # Check the password
        if user.check_password(password):
            print("Password is correct.")
            return user
        else:
            raise AuthenticationFailed("Incorrect password.")
