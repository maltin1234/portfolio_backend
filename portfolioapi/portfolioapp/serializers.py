# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Todo
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['description']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "completed","image", "project_description", "created", "user" ]
        
     