# users/urls.py
from django.urls import path
from .views import ProfileApiView

urlpatterns = [
    path('albania/', ProfileApiView.as_view(), name='profile_api_view'),
]