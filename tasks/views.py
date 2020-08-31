from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
# Delete
from django.core.exceptions import PermissionDenied
from django.urls import reverse

def index(request):
    """The home page for tasks."""
    return render(request, 'tasks/index.html')

@login_required
def projects(request):
    """ Show all Projects"""
    projects = Project.objects.filter(owner=request.user).order_by('date_added')
    context = {'projects': projects}
    return render(request, 'tasks/projects.html', context)

@login_required
def project(request, project_id):
    """Show a single project and all it's tasks."""
    project = Project.objects.get(id=project_id)
    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    tasks = project.task_set.order_by('-date_added')
    context = {'project':project, 'tasks': tasks}
    return render(request, 'tasks/project.html', context )

@login_required
def task(request, task_id):
    """Show a single task"""
    tasks = Task.objects.get(id=task_id)

    # Make sure the task belongs to the current user.
    project = tasks.project
    if project.owner != request.user:
        raise Http404

    context = {'tasks':tasks}
    return render(request, 'tasks/task.html', context)

@login_required
def new_project(request):
    """Add new project"""

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProjectForm()
    else:
        # POST data submitted; process data.
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.save()
            return redirect('tasks:projects')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tasks/new_project.html', context)


@login_required
def new_task(request, project_id):
    """ Add new task """
    project = Project.objects.get(id=project_id)

    # Make sure the task belongs to the current user.
    if project.owner != request.user:
        raise Http404

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


@login_required
def edit_task(request, task_id):
    """ Edit task """
    task = Task.objects.get(id=task_id)
    project = task.project

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

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

@login_required
def delete_task(request, task_id):
    """ Delete task """
    task = Task.objects.get(id=task_id)
    project = task.project

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method != 'POST':
        raise PermissionDenied
    else:
        # redir_url = reverse(
        #     "tasks:project",
        #     kwargs={"list_id": task.task_list.id, "list_slug": task.task_list.slug},
        # )
        task.delete()

        messages.success(request, "Task '{}' has been deleted".format(task_id))
        return redirect('tasks:projects')

    
