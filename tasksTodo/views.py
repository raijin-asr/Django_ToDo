from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def index(request):
    tasks= Task.objects.all().order_by('-id') # Get all tasks from the database
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
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        is_completed= False

        if title!= "" and due_date!= "" and due_time!= "":
            task= Task(
                title=title,
                description=description,
                due_date=due_date,
                due_time=due_time, 
                is_completed=is_completed)
            task.save() # Save the task to the database
            return redirect('index') # Redirect to the index page
    else:
        return render(request, 'add_task.html')

def delete_task(request,task_id):
    task= Task.objects.get(id=task_id) # Get the task from the database

    return render(request, 'delete.html',{
        "task": task, # Pass the task to the template
    })

def task_detail(request, task_id):
    task= Task.objects.get(id=task_id) # Get only one task from the database
    return render(request, 'task_detail.html',{
        'task': task # Pass the task to the template
    })

def toggle_complete(request, task_id):
    task= Task.objects.get(id=task_id) # Get the task from the database
    if task: # If the task exists
        task.is_completed= not task.is_completed # Toggle the is_completed field
        task.save() # Save the task to the database
    return redirect('index') # Redirect to the index page

def remove_task(request, task_id):
    task= Task.objects.get(id=task_id) # Get the task from the database
    if task:
        task.delete() # Delete the task from the database
        return redirect('index') # Redirect to the index page