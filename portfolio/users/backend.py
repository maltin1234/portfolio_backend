from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    """
    Custom authentication backend that allows login with email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        # Log the input username (which is expected to be the email)
        print(f"Attempting to authenticate user with email: {username}")
        
        try:
            # Assume `username` is actually the email
            user = UserModel.objects.get(email=username)
            print(f"User found: {user}")
        except UserModel.DoesNotExist:
            print("User not found.")
            return None

        # Check the password
        if user.check_password(password):
            print("Password is correct.")
            return user
        else:
            print("Incorrect password.")
            return None
