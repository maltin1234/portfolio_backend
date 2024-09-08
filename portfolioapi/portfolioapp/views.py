from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoListApiView(APIView):
    # Add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # List all todos
    def get(self, request, *args, **kwargs):
        """
        List all the todo items for the given requested user
        """
        todos = Todo.objects.filter(user=request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new todo
    def post(self, request, *args, **kwargs):
        """
        Create a Todo with the given todo data
        """
        data = {
            'title': request.data.get('title'),
            'completed': request.data.get('completed'),
            'description': request.data.get('description'),
            'image': request.FILES.get('image'),  # Use request.FILES for file uploads
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
