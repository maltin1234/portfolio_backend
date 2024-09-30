from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    """
    Custom authentication backend that allows login with email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Assume `username` is the email in this case
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None

        # Check the password
        if user.check_password(password):
            return user
        return None
