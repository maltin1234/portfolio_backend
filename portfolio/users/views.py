from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# ViewSet for user registration and profile
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer  # Use RegisterSerializer for registration
        return UserProfileSerializer  # Use UserProfileSerializer for profile management

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  # Anyone can register
        return [IsAuthenticated()]  # Only authenticated users can view/update profiles

    def get_object(self):
        # Return the logged-in user's instance for profile management
        return self.request.user
