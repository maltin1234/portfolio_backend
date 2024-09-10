from django.urls import re_path
from .views import (
    TodoListApiView, UserTodosSearchApiView
    )

urlpatterns = [
    re_path('todo', TodoListApiView.as_view()),
    re_path('^user/(?P<username>.+)/$', UserTodosSearchApiView.as_view()),

]