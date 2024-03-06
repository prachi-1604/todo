from django.shortcuts import render,redirect
from .models import Todo
from django.http import HttpResponse
from django.contrib import messages 
# Create your views here.

from .forms import TodoForm

def todo(request):
    todos=Todo.objects.order_by('-id')
    return render(request,'todo.html',{'todos':todos})


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Please fill in both title and description.')
    return redirect('/')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')


def register(request):
    return render(request,'register.html',{})

def loginpage(request):
    return render(request,'login.html',{})