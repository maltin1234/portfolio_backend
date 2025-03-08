from django.urls import re_path
from .views import (
    ProjectDeleteByIdApiView,
    ProjectPublicListApiView,
    ProjectListApiView,
    ProjectDetailApiView,
    ProjectSearchApiView,
    ProjectUpdateByIdApiView,
    ProjectUpdateByNameApiView,
    ProjectDeleteByNameApiView,
    ProjectCreateApiView,
)

urlpatterns = [
    # Public: Get all projects (No authentication required)
    re_path('projects/public', ProjectPublicListApiView.as_view(), name='public-projects'),

    # Authenticated User: List and Create projects
    re_path('user/projects/', ProjectListApiView.as_view(), name='user-projects'),

    # Search projects by title (No authentication required)
    re_path('projects/search/', ProjectSearchApiView.as_view(), name='search-projects'),

    # Update project by name (Authenticated users only)
    re_path('projects/update/', ProjectUpdateByNameApiView.as_view(), name='update-project-by-name'),

    # Delete project by name (Authenticated users only)
 
    re_path('projects/delete/<int:id>/', ProjectDeleteByIdApiView.as_view(), name='delete-project-by-id'),
    # Create a project by user (Authenticated users only)
    re_path('projects/create/', ProjectCreateApiView.as_view(), name='create-project'),
    
    re_path('projects/update/<int:id>/', ProjectUpdateByIdApiView.as_view(), name='update-project-by-id'),
]  
