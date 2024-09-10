from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

class TodoListApiView(APIView):
    # Add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # List all todos
    def get(self, request, *args, **kwargs):
        """
        List all the todo items for the given requested user
        """
        todos = Todo.objects.filter(user=self.request.user)
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
            'project_description': request.data.get('project_description'),
            'image': request.FILES.get('image'),  # Use request.FILES for file uploads
        }
    
        serializer = TodoSerializer(data=data)  # Pass the data here

        if serializer.is_valid():
            # Save the instance and associate the user
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTodosSearchApiView(generics.ListAPIView):
    serializer_class = TodoSerializer  # Correct attribute name
    
    def get_queryset(self):
        """
        This view should return a list of all todos for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs.get('username')
        if not username:
            return Todo.objects.none()
        
        return Todo.objects.filter(user__username=username)
    
    def get(self, request, *args, **kwargs):
        """
        Override the get method to handle potential serializer errors.
        """
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "No todos found for this user."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
