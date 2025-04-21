# users/views.py
from rest_framework import generics, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer

class ProfileApiView(generics.ListCreateAPIView):
    """
    Retrieve or create the authenticated user's profile.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only the profile of the authenticated user
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Create the profile for the authenticated user
        serializer.save(user=self.request.user)
