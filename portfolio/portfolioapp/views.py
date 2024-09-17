from venv import logger
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Todo
from .serializers import TodoSerializer

class TodoListApiView(generics.ListCreateAPIView):
    """
    List all todo items for the authenticated user or create a new todo.
    """
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of all todos for the authenticated user.
        """
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the new todo item with the authenticated user.
        """
        serializer.save(user=self.request.user)

class TodoDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todo item.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter todos to ensure that users can only access their own todos.
        """
        return Todo.objects.filter(user=self.request.user)
    


class UserTodosSearchApiView(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned todos to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Todo.objects.all()
        username = self.request.query_params.get('user')  # Get the 'user' query param, assuming it's the username

        if username is not None:
            # Filter by the 'username' field of the related User model
            queryset = queryset.filter(user__username=username)

        return queryset
