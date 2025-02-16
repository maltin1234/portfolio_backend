from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import Rating
from .serializers import RatingSerializer, RegisterSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import action  # Add this import
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from django.db.models import Avg  # Import Avg for calculating average
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
CustomUser = get_user_model()
#########################################################


#ViewSet for user registration and profile management
class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoints:
    - POST    http://127.0.0.1:8080/users/           -> Register a new user
    - GET     http://127.0.0.1:8080/users/<username>/ -> Retrieve a user's profile (public)
    - GET     http://127.0.0.1:8080/users/user/       -> Retrieve the logged-in user's profile
    - PATCH   http://127.0.0.1:8080/users/user/       -> Update the logged-in user's profile
    - GET     http://127.0.0.1:8080/users/all_users/  -> Get all users
    - Delete  http://127.0.0.1:8080/users/delete_user/  -> Delete user
    - POST    http://127.0.0.1:8080/users/<user_id>/add_rating/    -> Add a rating for a specific user
    - GET     http://127.0.0.1:8080/users/<username>/view_ratings/ -> View all ratings for a specific use
    """
    
    queryset = CustomUser.objects.all()  # Fetch all users

    #Depending on the action (e.g., create, retrieve), use a different serializer
    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer  # Serializer for user registration
        return UserProfileSerializer  # Serializer for user profile

    #Define permission rules based on the action
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  # Anyone can register a new user
        elif self.action == 'retrieve':
            return [AllowAny()]  # Anyone can retrieve a user's profile
        return [AllowAny()]  # Other actions require authentication
    
   # Retrieve a user's profile by their username
    #API route: GET http://127.0.0.1:8080/users/<username>/
    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.filter(username=pk)  # Filter by username
        user = get_object_or_404(queryset, username=pk)  # Return 404 if user not found
        serializer = UserProfileSerializer(user)  # Serialize user data
        return Response(serializer.data)  # Return user profile in response

    #Custom action to retrieve the logged-in user's profile
    #API route: GET http://127.0.0.1:8080/users/user/
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def retrieve_self(self, request):
        """Retrieve the profile of the currently logged-in user."""
        user = request.user  # Get the logged-in user
        serializer = UserProfileSerializer(user)  # Serialize user profile
        return Response(serializer.data)  # Return logged-in user's profile in response

    #Custom action to update the logged-in user's profile (PATCH method)
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

#Custom action to retrieve all users
    #API route: GET http://127.0.0.1:8080/users/all_users/
    @action(detail=False, methods=['get'])
    def all_users(self, request):
        """Retrieve a list of all users."""
        users = CustomUser.objects.all()  # Get all users
        serializer = UserProfileSerializer(users, many=True)  # Serialize all users
        return Response(serializer.data)  # Return the list of users in response
    
    @action(detail=True, methods=['delete'])
    def delete_user(self, request, pk=None):
        """Delete a specific user."""
        user = get_object_or_404(CustomUser, username=pk)  # Get the user by ID or username
        user.delete()  # Delete the user
        return Response({"detail": "User deleted successfully."}, status=HTTP_204_NO_CONTENT)
    

    @action(detail=True, methods=['post'])
    def add_rating(self, request, pk=None):
        """Add a rating for a specific user."""
        user = get_object_or_404(CustomUser, username=pk)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)  # Associate the rating with the user
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    @action(detail=True, methods=['get'])
    def view_ratings(self, request, pk=None):
        """View all ratings for a specific user with their average rating."""
        user = get_object_or_404(CustomUser, username=pk)
        
        #Fetch all ratings for the user
        ratings = Rating.objects.filter(user=user)
        
       # Calculate the average rating
        avg_rating = ratings.aggregate(avg_rating=Avg('rating'))['avg_rating']
        avg_rating = round(avg_rating, 2) if avg_rating else None
        
        #Serialize the ratings
        serializer = RatingSerializer(ratings, many=True)
        
       # Include the average rating in the response
        response_data = {
            "average_rating": avg_rating,
            "ratings": serializer.data
        }
        
        return Response(response_data)
@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)





