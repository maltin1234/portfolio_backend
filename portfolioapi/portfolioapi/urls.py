"""
URL configuration for portfolioapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from portfolioapp import urls as todo_urls
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
     re_path('admin/', admin.site.urls),
     re_path('api-auth/', include('rest_framework.urls')),
     re_path('api/todos', include(todo_urls)),
     re_path('api/users', include('users.urls')),
     re_path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     re_path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  
] 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
