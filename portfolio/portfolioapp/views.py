from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer

# Public View: Get all projects (No authentication required)
class ProjectPublicListApiView(generics.ListAPIView):
    """
    Publicly accessible endpoint to retrieve all projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required

  
# Authenticated User's Projects
class ProjectListApiView(generics.ListCreateAPIView):
    """
    List all Project items for the authenticated user or create a new Project.
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve, update, or delete a project (filtered by user)
class ProjectDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


# Search Projects by Name
class ProjectSearchApiView(generics.ListAPIView):
    """
    Search for projects by name. Can be used to search by 'title' query parameter.
    """
    serializer_class = ProjectSerializer
    permission_classes = []  # Public access

    def get_queryset(self):
        queryset = Project.objects.all()
        title = self.request.query_params.get('title', None)

        if title:
            queryset = queryset.filter(title__icontains=title)  # Case-insensitive search

        return queryset

class ProjectCreateApiView(generics.CreateAPIView):
    """
    API endpoint that allows users to create a new project.
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Assign the authenticated user to the new project.
        """
        serializer.save(user=self.request.user)
        
# Update Project by Name
class ProjectUpdateByNameApiView(generics.UpdateAPIView):
    """
    Update a project by its title. Only the owner can update.
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        title = self.kwargs.get("title")  # URL parameter
        project = get_object_or_404(Project, title=title, user=self.request.user)
        return project


# Delete Project by ID
class ProjectDeleteByIdApiView(generics.DestroyAPIView):
    """
    Delete a project by its ID. Only the owner can delete.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        project_id = self.kwargs.get("id")  # Extract ID from URL
        project = get_object_or_404(Project, id=project_id, user=self.request.user)
        return project

class ProjectUpdateByIdApiView(generics.UpdateAPIView):
    """
    Update a project by its ID. Only the owner can update.
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        project_id = self.kwargs.get("id")  # Extract ID from URL
        project = get_object_or_404(Project, id=project_id, user=self.request.user)
        return project
