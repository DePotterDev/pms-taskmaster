from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm

def index(request):
    """The home page for tasks."""
    return render(request, 'tasks/index.html')

def projects(request):
    """ Show all Projects"""
    projects = Project.objects.order_by('date_added')
    context = {'projects': projects}
    return render(request, 'tasks/projects.html', context)

def project(request, project_id):
    """Show a single project and all it's tasks."""
    project = Project.objects.get(id=project_id)
    tasks = project.task_set.order_by('-date_added')
    context = {'project':project, 'tasks': tasks}
    return render(request, 'tasks/project.html', context )

def task(request, task_id):
    """Show a single task"""
    tasks = Task.objects.get(id=task_id)
    context = {'tasks':tasks}
    return render(request, 'tasks/task.html', context)

def new_project(request):
    """Add new project"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProjectForm()
    else:
        # POST data submitted; process data.
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:projects')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tasks/new_project.html', context)


def new_task(request, project_id):
    """ Add new task """
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TaskForm()
    else:
        # POST data submitted; process data.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.project = project
            new_task.save() 
            return redirect('tasks:project', project_id=project_id)

    # Display a blank or invalid form.
    context = {'project': project, 'form': form}
    return render(request, 'tasks/new_task.html', context)


def edit_task(request, task_id):
    """ Edit task """
    task = Task.objects.get(id=task_id)
    project = task.project

    if request.method != 'POST':
        # No data submitted; create form with pre-filled entry.
        form = TaskForm(instance=task)
    else:
        # POST data submitted; process data.
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:project', project_id=project.id)
    
    context = {'task': task, 'project': project, 'form': form}
    return render(request, 'tasks/edit_task.html', context)
    
