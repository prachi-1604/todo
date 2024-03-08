# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .views import *
from django.shortcuts import get_object_or_404


def todo(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        inprogress_todos = Todo.objects.filter(status="inprogress")
        review_todos = Todo.objects.filter(status="review")
        done_todos = Todo.objects.filter(status="done")
    return render(request, 'todo.html', {'todo': todo, 'inprogress_todos': inprogress_todos,'review_todo':review_todos,'done_todo':done_todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', 'inprogress')
        todo= Todo.objects.create(title=title, description=description, status=status)
        return redirect('todo')
    return render(request, 'todo.html')  # Handle GET requests

def update_todo_status(request, todo_id, new_status):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.status = new_status
        todo.save()
        return JsonResponse({'message': 'Task status updated successfully.'})
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Task not found.'}, status=404)

def delete_todo(request, todo_id):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return redirect('todo')

def move_todo_status(request, todo_id, new_status):
    
    todo = get_object_or_404(Todo, id=todo_id)
    todo.status = new_status
    todo.save()

    return JsonResponse({'message': 'Todo status updated successfully'})

def advanceTodo(request,todo_id,new_status):
    try:
        todo = Todo.objects.get(Todo,pk=todo_id)
        todo.status = new_status
        todo.save()
        return JsonResponse({'message': 'Task status updated successfully.'})
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Task not found.'}, status=404)