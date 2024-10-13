from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import action  # Add this import

from rest_framework.response import Response

CustomUser = get_user_model()

# ViewSet for user registration and profile management
class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoints:
    - POST    http://127.0.0.1:8080/users/           -> Register a new user
    - GET     http://127.0.0.1:8080/users/<username>/ -> Retrieve a user's profile (public)
    - GET     http://127.0.0.1:8080/users/user/       -> Retrieve the logged-in user's profile
    - PATCH   http://127.0.0.1:8080/users/user/       -> Update the logged-in user's profile
    """

    queryset = CustomUser.objects.all()  # Fetch all users

    # Depending on the action (e.g., create, retrieve), use a different serializer
    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer  # Serializer for user registration
        return UserProfileSerializer  # Serializer for user profile

    # Define permission rules based on the action
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  # Anyone can register a new user
        elif self.action == 'retrieve':
            return [AllowAny()]  # Anyone can retrieve a user's profile
        return [IsAuthenticated()]  # Other actions require authentication
    
    # Retrieve a user's profile by their username
    # API route: GET http://127.0.0.1:8080/users/<username>/
    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.filter(username=pk)  # Filter by username
        user = get_object_or_404(queryset, username=pk)  # Return 404 if user not found
        serializer = UserProfileSerializer(user)  # Serialize user data
        return Response(serializer.data)  # Return user profile in response

    # Custom action to retrieve the logged-in user's profile
    # API route: GET http://127.0.0.1:8080/users/user/
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def retrieve_self(self, request):
        """Retrieve the profile of the currently logged-in user."""
        user = request.user  # Get the logged-in user
        serializer = UserProfileSerializer(user)  # Serialize user profile
        return Response(serializer.data)  # Return logged-in user's profile in response

    # Custom action to update the logged-in user's profile (PATCH method)
    # API route: PATCH http://127.0.0.1:8080/users/user/
    @action(detail=False, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_self(self, request):
        """Update the profile of the currently logged-in user."""
        user = request.user  # Get the logged-in user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()  # Save the updated profile
            return Response(serializer.data)  # Return updated profile
        return Response(serializer.errors, status=400)  # Return errors if validation fails
