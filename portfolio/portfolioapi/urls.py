from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,

# )
# from allauth.socialaccount.providers.github import views as github_view
from django.contrib import admin
from django.urls import include, path
# from users.views import UserViewSet, secret_page  # Import the secret_page view





# Initialize the router and register your viewset
router = DefaultRouter()
# router.register('users', UserViewSet, basename='users')

# Merged urlpatterns, making sure to include both sets of routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('portfolioapp.urls')),  # Don't forget to include the trailing slash
    # re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # re_path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
   

    #####################

    # re_path('dj-rest-auth/github/', GitHubLogin.as_view(), name='github_login'),
    # path('api/auth/github/login/', github_views.oauth2_login, name='github_login'),
    # path('api/auth/github/login/callback/', github_views.oauth2_callback, name='github_callback'),
    # Include the API endpoints:
  
    # path('secret', secret_page, name='secret'),  # Fix the URL pattern and reference the view
    # Include the router URLs for user-related views
    path('', include(router.urls)),  
]

# Serve media files in development mode
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
