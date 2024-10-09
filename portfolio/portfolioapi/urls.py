from django.urls import re_path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserViewSet

# Initialize the router and register your viewset
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

# Merged urlpatterns, making sure to include both sets of routes
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api-auth/', include('rest_framework.urls')),
    re_path('api/todos/', include('portfolioapp.urls')),  # Don't forget to include the trailing slash
    re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include the router URLs for user-related views
    re_path('', include(router.urls)),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
