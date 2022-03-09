
from django.urls import path
from .views import  todolist, delete_task, complete_task, incomplete_task, edit_task

urlpatterns = [
    path('todolist/', todolist, name='todolist'),
    path('todolist/delete/<task_id>', delete_task, name='delete_task'),
    path('todolist/complete/<task_id>',complete_task, name='complete_task'),
    path('todolist/incomplete/<task_id>',incomplete_task, name='incomplete_task'),
    path('todolist/edit/<task_id>', edit_task, name='edit'),
]
