from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.TODOView.as_view(), name="todo_url"),
    path('tasks/', views.TODOListView.as_view(), name="task_list_url"),
]
