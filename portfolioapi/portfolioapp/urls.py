from django.urls import re_path
from .views import TodoListApiView, TodoDetailApiView, UserTodosSearchApiView

urlpatterns = [
    # URL for listing and creating todos
    re_path('todos/', TodoListApiView.as_view(), name='todo_list_create'),

    # URL for retrieving, updating, and deleting a specific todo
    re_path('^tod/(?P<pk>\d+)/$', TodoDetailApiView.as_view(), name='todo_detail'),

    # URL for searching todos by username
    re_path('todotitle', UserTodosSearchApiView.as_view()),
]

