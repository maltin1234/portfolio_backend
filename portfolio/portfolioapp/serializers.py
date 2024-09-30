# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "completed","image", "project_description", "created", "user" ]
        
     