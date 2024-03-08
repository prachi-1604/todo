# urls.py

from django.urls import path
from .views import todo, create_todo, delete_todo, move_todo_status,update_todo_status,advanceTodo



urlpatterns = [
    path('',todo, name='todo'),
    path('create_todo/', create_todo, name='create_todo'),
    path('delete_todo/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('update_todo_status/<str:todo_id>/<str:new_status>/', update_todo_status, name='update_todo_status'),
    path('move_todo_status/<str:todo_id>/<str:new_status>/', move_todo_status, name='move_todo_status'),
    path('advanceTodo/<str:todo_id>/<str:new_status>/', advanceTodo, name='advanceTodo'),
]
