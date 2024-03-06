from django.urls import path
from todo.views import *
urlpatterns = [
    path('',todo),
    path('create_todo/', create_todo, name='create_todo'),
    path('delete_todo/<int:todo_id>', delete_todo, name='delete_todo'),
    path('register/',register,name='register'),
    path('login/',loginpage,name='login'),
]