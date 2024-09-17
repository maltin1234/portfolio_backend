from django.urls import re_path
from .views import ProfileDetailView, RegisterView, UserInfoApiView


urlpatterns = [
    re_path('register/', RegisterView.as_view(), name='register'),
    re_path('profile/', ProfileDetailView.as_view(), name='profile'),
    re_path('userinfo/', UserInfoApiView.as_view(), name='userinfo'),
]