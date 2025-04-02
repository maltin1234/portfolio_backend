# from django.urls import path
# from .views import CustomUserCreate

# app_name = 'users'

# urlpatterns = [
#     path('create/', CustomUserCreate.as_view(), name="create_user"),
# ]
from django.urls import path
from .views import (
    RegisterUserView,
    UserProfileView,
    RetrieveSelfView,
    UpdateSelfView,
    AllUsersView,
    AddRatingView,
    ViewRatingsView
)

app_name = 'users'

urlpatterns = [
    # User registration
    path('register/', RegisterUserView.as_view(), name="register_user"),

    # Retrieve, update, and delete a user by username
    # path('<str:username>/', UserProfileView.as_view(), name="user_profile"),

    # Retrieve the logged-in user's profile
    path('self/', RetrieveSelfView.as_view(), name="self_profile"),

    # Update the logged-in user's profile
    path('self/update/', UpdateSelfView.as_view(), name="update_self"),

    # Get all users
    path('all/', AllUsersView.as_view(), name="all_users"),

    # Add a rating to a user
    path('<str:username>/add_rating/', AddRatingView.as_view(), name="add_rating"),
 
    # View all ratings of a user
    path('<str:username>/view_ratings/', ViewRatingsView.as_view(), name="view_ratings"),
]
