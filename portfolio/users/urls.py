from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# If using ModelViewSet
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    re_path('', include(router.urls)),
]
