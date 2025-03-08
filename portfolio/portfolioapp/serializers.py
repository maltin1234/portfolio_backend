# Project/Project_api/serializers.py
from rest_framework import serializers
from .models import Project
from django.contrib.auth import get_user_model

#CustomUser = get_user_model()
CustomUser = get_user_model()
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "completed","image", "project_description", "created","link_url","github_url","tags" ]
        
     