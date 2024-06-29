from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    tasks= Task.objects.all() # Get all tasks from the database
    return render(request, 'index.html',{ 
        'tasks': tasks # Pass the tasks to the template
    })

def completed_task(request):
    completed_tasks= Task.objects.filter(is_completed=True) # Get all completed tasks from the database

    return render(request, 'completed.html',{
        'completed_tasks': completed_tasks # Pass the completed tasks to the template
    })

def remaining_task(request):
    remaining_task= Task.objects.filter(is_completed=False) # Get all remaining tasks from the database

    return render(request, 'remaining.html',{
        'remaining_task': remaining_task
    })

def add_task(request):
    return render(request, 'add_task.html')

def delete_task(request):
    return render(request, 'delete.html')

def task_detail(request):
    return render(request, 'task_detail.html')