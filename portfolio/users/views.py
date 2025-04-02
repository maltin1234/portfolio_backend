from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Rating
from .serializers import RatingSerializer, RegisterSerializer, UserProfileSerializer

CustomUser = get_user_model()


# ✅ Register a new user (POST)
class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can register


# ✅ Retrieve, update, or delete a specific user (GET, PATCH, DELETE)
class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'  # Allow lookup by username

    def get_permissions(self):
        """Publicly accessible user profiles but only authenticated users can update/delete themselves"""
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def delete(self, request, *args, **kwargs):
        """Allow a user to delete their own account"""
        user = self.get_object()
        if request.user != user:
            return Response({"detail": "You can only delete your own account."}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)


# ✅ Retrieve the logged-in user's profile (GET)
class RetrieveSelfView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        print(serializer.data)
        return Response(serializer.data)


# ✅ Update the logged-in user's profile (PATCH)
class UpdateSelfView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ List all users (GET)
class AllUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'email'


# ✅ Add a rating for a user (POST)
class AddRatingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ View all ratings of a user (GET)
class ViewRatingsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        ratings = Rating.objects.filter(user=user)
        avg_rating = ratings.aggregate(avg_rating=Avg('rating'))['avg_rating']
        avg_rating = round(avg_rating, 2) if avg_rating else None
        serializer = RatingSerializer(ratings, many=True)
        
        return Response({"average_rating": avg_rating, "ratings": serializer.data})


# ✅ Secret Page (Protected with Login)
@login_required
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)
