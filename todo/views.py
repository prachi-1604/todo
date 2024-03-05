from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def todo(request):
    todos=Todo.objects.order_by('-id')
    return render(request,'todo.html',{'todos':todos})

def create_todo(request):
    if request.method=='POST':
        title= request.POST.get('title')
        description= request.POST.get('description')
        Todo.objects.create(title=title, description=description)
    return redirect('/')

def complete_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('/')
    
def delete_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')
