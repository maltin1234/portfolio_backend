from django.urls import re_path
from .views import (
    TodoListApiView,
)

urlpatterns = [
    re_path('api', TodoListApiView.as_view()),
]